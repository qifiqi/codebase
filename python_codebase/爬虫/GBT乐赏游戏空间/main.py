import requests
import queue
import pymysql
from parsel import Selector
from hashlib import md5
from concurrent.futures import ThreadPoolExecutor

id_q = queue.Queue()
parser_q = queue.Queue()


class GetResponse():

    def __init__(self, id_q, parser_q):
        self.session = requests.session()
        self.urls = "http://cb.ysepan.com/f_ht/ajcx/wj.aspx?cz=dq&jsq=0&mlbh=%s&wjpx=1&_dlmc=gbtgame&_dlmm="
        self.head = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '__yjs_duid=1_ad3296e8a4c479f21e80ff3a28bfdd2f1672403595382; ASP.NET_SessionId=ng2gmrvcnhevnvhzeeb3mfko',
            'Host': 'cb.ysepan.com',
            'Pragma': 'no-cache',
            'Referer': 'http://cb.ysepan.com/f_ht/ajcx/000ht.html?bbh=1165',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',

        }
        self.proxy_num = 0
        self.id_q = id_q
        self.parser_q = parser_q
        self._get_id()

    def get_response(self, mlbh=None):
        if self.id_q.empty():
            return ""
        if not mlbh:
            if self.id_q.qsize() < 0:
                return
            mlbh = self.id_q.get(block=False)
        print(mlbh)
        self.session.get("http://zy.ysepan.com/f_zy/tp/wjlx/eye.gif", headers=self.head)
        try:
            response = self.session.get(
                url=(self.urls % mlbh),
                headers=self.head,
                proxies=self.get_proxy(),
                timeout=5
            )
        except Exception as e:
            print(e)
            print("超时", mlbh)
            self.get_response(mlbh)
            return
        if response.status_code == 209:
            self.parser_q.put(
                response.content.decode("utf-8").split("]", 1)[-1]
            )
            self.id_q.task_done()
        else:
            print("重试",mlbh)
            self.get_response(mlbh)

    def get_proxy(self):
        url = "http://xiaofubase.top:5010/get/"
        proxy_response = requests.get(url)
        if proxy_response.status_code == 200:
            try:
                proxy_response_json = proxy_response.json()
            except Exception as e:
                print(e)
            else:
                if proxy_response_json.get("https"):
                    return {
                        "http": "http://" + proxy_response_json.get("proxy"),
                        "https": "https://" + proxy_response_json.get("proxy")
                    }
                else:
                    return {
                        "http": "http://" + proxy_response_json.get("proxy")
                    }
        else:
            if self.proxy_num < 3:
                self.proxy_num += 1
                self.get_proxy()
            else:
                return {}

    def _get_id(self):
        url = "http://cb.ysepan.com/f_ht/ajcx/ml.aspx?cz=ml_dq&_dlmc=gbtgame&_dlmm="
        response = self.session.get(url, headers=self.head)
        response = response.content.decode("utf-8").split("]", 1)[-1]
        html = Selector(response)
        for li in html.css("li"):
            num_id = li.css("::attr(id)").get("").split("_")[-1]
            self.id_q.put(num_id)

        self.id_q_len = self.id_q.qsize()


class parserSql():
    def __init__(self, id_q, parser_q):
        self.conn = pymysql.connect(
            user="root",
            password="123123",
            host="localhost",
            port=3306,
            db="text_db"
        )
        self.cursor = self.conn.cursor()
        self._create_databases()
        self.id_q = id_q
        self.parser_q = parser_q

    def _create_databases(self):
        sql = """
            CREATE TABLE IF NOT EXISTS `game_tables` (#判断这张表是否存在，若存在，则跳过创建表操作，
             `g_id` varchar(40) NOT NULL, 
            `g_name` varchar(255) default NULL, 
            `g_href` varchar(255) default NULL, 
            `g_title` varchar(255) default NULL, 
            `g_num` varchar(255) default NULL, 
            `g_tag` varchar(255) default NULL, 
            PRIMARY KEY (`g_id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;

        """
        self.cursor.execute(sql)
        self.conn.commit()

    def parse_html(self):
        if self.parser_q.qsize() < 0:
            return
        content = self.parser_q.get(block=False)
        if not content:
            return

        response = Selector(content)
        self.parser_q.task_done()

        for li in response.css("li"):
            data = dict()
            g_name = li.css("a::text").get("")
            if g_name:
                data["g_name"] = g_name

            g_id = li.css("::attr(id)").get("")
            if g_id:
                data["g_id"] = g_id.split("_")[-1]
            else:
                data["g_id"] = md5(g_name.encode("utf-8")).hexdigest()
            data["g_href"] = li.css("a::attr(href)").get("")
            data["g_title"] = li.css("a::attr(title)").get("")
            data["g_num"] = li.css("i::text").get("")
            data["g_tag"] = li.css("b::text").get("")

            print(data)
            if all(data):
                sql = f"""INSERT IGNORE INTO `game_tables` VALUES ('{data["g_id"]}', '{data["g_name"]}', '{data["g_href"]}', '{data["g_title"]}','{data["g_num"]}','{data["g_tag"]}');"""
                self.cursor.execute(sql)
                self.conn.commit()

    def clone_sql(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':

    g = GetResponse(id_q, parser_q)
    print(g.id_q_len)
    while g.id_q.qsize() > 0:
        g.get_response()

    p = parserSql(id_q, parser_q)
    while p.parser_q.qsize() > 0:
        p.parse_html()
