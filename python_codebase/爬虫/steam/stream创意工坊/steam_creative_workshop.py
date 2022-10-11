# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2318:59
# @Author  : 小符玩代码
# @Email   : 2737454073@qq.com
# @File    : steam_creative_workshop.py
# @Software: PyCharm
import datetime
import queue
import re
import sys
import time

import faker
import pymysql
import requests
import logging
import urllib.parse
from lxml import etree
from threading import Thread
from threading import Lock

# 方式一
"""
# 格式
form = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                         datefmt='%Y-%m-%d %H:%M:%S %p',
                         )
# 初始化程序
Stream = logging.StreamHandler()
# 设置初始化格式
Stream.setFormatter(form)
# 设置日志等级
Stream.setLevel(20)
# 取出日志
l1 = logging.getLogger('root')
"""
# 方式二


c_queue = queue.Queue()
p_queue = queue.Queue()

lock = Lock()

logging.basicConfig(
    filename='./steam.log',
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s -%(threadName)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=20,

)
type = 'Mature'


def log(text):
    """
    写日志
    @param text:
    """
    logging.error(text)


def character_handling(character: str) -> str:
    """
    处理特殊字符
    @param character: str
    @return: str
    """
    com = re.compile('[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]')
    return com.sub('', character)


class threading_father(Thread):
    def __init__(self, p_queue, c_queue, name, daemon=True):
        super().__init__(daemon=daemon)
        self.name = name
        self.c_queue = c_queue
        self.p_queue = p_queue
        self.fa = faker.Faker('zh_CN')
        self.head = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.2; en-US; Valve Steam Client/default/1654574690; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'Cookie': 'timezoneOffset=28800,0; _ga=GA1.2.940594228.1649389155; browserid=2541727184154055939; steamMachineAuth76561199034509976=D2F4E13358FCB45178EE065A0315FCA73696A33E; recentlyVisitedAppHubs=977950%2C431960; Steam_Language=schinese; steamLogin=76561199034509976%7c%7cCF71E77AD66F7C3BFBD5E926CD386C2E2F82EC8E; sessionid=bce6a38d246d86c9fca64356; steamLoginSecure=76561199034509976%7c%7c11930E28EF1218DD42FC41E2C4D38CD92F9A8BEB; clientsessionid=2dee100e0518bf2a; _gid=GA1.2.190111330.1658803513; app_impressions=431960@2_100100_100101_100103|431960@2_100100_100101_100103|431960@2_9_100000_|431960@2_9_100013_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_,',
            'Referer': 'https://steamcommunity.com/workshop/browse/?appid=431960&browsesort=trend&section=readytouseitems&days=90&actualsort=trend&p=1',
            'Connection': 'close'
        }
        self.conn = pymysql.Connect(
            user='root',
            password='123123',
            port=3306,
            host='localhost',
            db='text_db',
        )
        self.cursor = self.conn.cursor()


class producer_steam(threading_father):
    def __init__(self, p_queue, c_queue, name):
        self.__quit_all = False
        super().__init__(p_queue, c_queue, name)

    def run(self) -> None:
        while True:
            if self.__quit_all:
                break
            self.get_steam()

    def terminate(self):
        self.__quit_all = True

    def get_steam(self):
        try:
            url = p_queue.get()
            response = requests.get(url, headers=self.head, timeout=10, verify=False).text
            self.head['Referer'] = url
            c_queue.put(response)
        except Exception as e:
            log(e)


class consumer_steam(threading_father):
    pass

    def __init__(self, p_queue, c_queue, name):
        super().__init__(p_queue, c_queue, name)
        self.__quit_all = False

    def run(self) -> None:
        while True:
            if self.__quit_all:
                self.cursor.close()
                self.conn.close()
                sys.exit()
            self.html_Parse(c_queue.get())

    def terminate(self):
        self.__quit_all = True

    def html_Parse(self, data_text):
        """
            解析主页
            @return: 解析的数据
            """
        html = etree.HTML(data_text)
        div_list = html.xpath('//div[@id="profileBlock"]/div/div[3]/div')
        for div in div_list:
            try:
                href = div.xpath('./a[@class="ugc"]/@href')[0]
                appid = div.xpath('./a/@data-appid')[0]
                publishedfileid = div.xpath('./a/@data-publishedfileid')[0]
                img_path = div.xpath('.//img[@class="workshopItemPreviewImage "]/@src')[0]
                grade_img_path = div.xpath('./img[@class="fileRating"]/@src')[0]
                grade = grade_img_path.split('/')[-1][0]
                title = character_handling(div.xpath('./a[@class="item_link"]/div/text()')[0])
                author = character_handling(div.xpath('./div[@class="workshopItemAuthorName ellipsis"]/a/text()')[0])
                data = (appid,
                        publishedfileid,
                        grade,
                        title,
                        author,
                        href,
                        img_path,
                        type,
                        str(datetime.datetime.now()).split('.')[0])
                if not all(data):
                    continue
            except IndexError as execs:
                log(execs)
                continue
            else:
                sql = """REPLACE into steam values ("%s","%s","%s","%s","%s","%s","%s","%s","%s");""" % data
                self.cursor.execute(sql)
        else:
            self.conn.commit()


def url_queue(type_num=1):
    global type
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.2; en-US; Valve Steam Client/default/1654574690; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Cookie': 'timezoneOffset=28800,0; _ga=GA1.2.940594228.1649389155; browserid=2541727184154055939; steamMachineAuth76561199034509976=D2F4E13358FCB45178EE065A0315FCA73696A33E; recentlyVisitedAppHubs=977950%2C431960; Steam_Language=schinese; steamLogin=76561199034509976%7c%7cCF71E77AD66F7C3BFBD5E926CD386C2E2F82EC8E; sessionid=bce6a38d246d86c9fca64356; steamLoginSecure=76561199034509976%7c%7c11930E28EF1218DD42FC41E2C4D38CD92F9A8BEB; clientsessionid=2dee100e0518bf2a; _gid=GA1.2.190111330.1658803513; app_impressions=431960@2_100100_100101_100103|431960@2_100100_100101_100103|431960@2_9_100000_|431960@2_9_100013_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_,',
        'Referer': 'https://steamcommunity.com/workshop/browse/?appid=431960&browsesort=trend&section=readytouseitems&days=90&actualsort=trend&p=1',
        'Connection': 'close'
    }
    if type_num == 1:
        url = 'https://steamcommunity.com/workshop/browse/'
        data = {
            'appid': '431960',
            'browsesort': 'mostrecent',
            'section': 'readytouseitems',
            'days': '90',
            'actualsort': 'mostrecent',
            'p': 1

        }
        url_path = '?'.join((url, urllib.parse.urlencode(data)))

        response = requests.get(url_path, headers=head, timeout=10, verify=False).text
        html = etree.HTML(response)
        maxpage = html.xpath('//*[@id="profileBlock"]/div/div[4]/div[2]/a[6]/text()')[0]

        for i in range(1, maxpage + 1):
            """
                appid=431960 软件ip
                browsesort=trend \ mostrecent
                section=readytouseitems
                days=90
                actualsort=trend\mostrecent
                p=1000 页数
            """
            data = {
                'appid': '431960',
                'browsesort': 'mostrecent',
                'section': 'readytouseitems',
                'days': '90',
                'actualsort': 'mostrecent',
                'p': i

            }
            url_path = '?'.join((url, urllib.parse.urlencode(data)))
            p_queue.put(url_path)
        type = '最新十八以上'
    elif type_num == 2:
        url ='https://steamcommunity.com/workshop/browse/?appid=431960&searchtext=&childpublishedfileid=0&browsesort=mostrecent&section=readytouseitems&requiredtags%5B0%5D=Mature&requiredtags%5B1%5D=Girls&created_date_range_filter_start=0&created_date_range_filter_end=0&updated_date_range_filter_start=0&updated_date_range_filter_end=0&actualsort=mostrecent&p=1'
        response = requests.get(url, headers=head, timeout=10, verify=False).text
        html = etree.HTML(response)
        maxpage = html.xpath('//*[@id="profileBlock"]/div/div[4]/div[2]/a[3]/text()')[0]
        for i in range(1, int(maxpage) + 1):
            # data = {
            #     'appid': '431960',  # 软件id
            #     'searchtext': '',
            #     'childpublishedfileid': 0,
            #     'browsesort': 'mostrecent',  # 设置最新
            #     'section': 'readytouseitems',
            #     # 'requiredtags%5B0%5D': 'Mature',  # 类型
            #     'requiredtags%5B0%5D': 'Girls&requiredtags%5B1%5D=Mature',  # 类型
            #     'created_date_range_filter_start': 0,  # 设置创作开始时间
            #     'created_date_range_filter_end': 0,  # 设置结束
            #     'updated_date_range_filter_start': 0,  # 设置更新时间
            #     'updated_date_range_filter_end': 0,  # 设置结束
            #     'actualsort': 'mostrecent',
            #     'p': i
            # }
            url_path = f'https://steamcommunity.com/workshop/browse/?appid=431960&searchtext=&childpublishedfileid=0&browsesort=mostrecent&section=readytouseitems&requiredtags%5B0%5D=Mature&requiredtags%5B1%5D=Girls&created_date_range_filter_start=0&created_date_range_filter_end=0&updated_date_range_filter_start=0&updated_date_range_filter_end=0&actualsort=mostrecent&p={i}'
            # url_path = '?'.join((url, urllib.parse.urlencode(data)))
            p_queue.put(url_path)
        type = '最新十八以上,Girls'

    # break


def main():
    url_queue(2)
    p_list = []
    c_list = []

    for i in range(10):
        p = producer_steam(p_queue=p_queue, c_queue=c_queue, name=f'producer_{i}')
        p.start()
        p_list.append(p)

    for i in range(3):
        c = consumer_steam(p_queue=p_queue, c_queue=c_queue, name=f'consumer_{i}')
        c.start()
        c_list.append(c)

    while True:
        time.sleep(32)
        print('p_queue.empty() and p_queue.qsize()==0', p_queue.empty() and p_queue.qsize() == 0)
        print('c_queue.empty() and c_queue.qsize()==0', c_queue.empty() and c_queue.qsize() == 0)
        print('p_queue.empty() and c_queue.empty()', p_queue.empty() and c_queue.empty())

        if p_queue.empty() and p_queue.qsize() == 0:
            if c_queue.empty() and c_queue.qsize() == 0:
                for c in c_list:
                    c.terminate()
            for p in p_list:
                p.terminate()
        if p_queue.empty() and c_queue.empty():
            break


if __name__ == '__main__':
    main()
    # url_queue(2)
