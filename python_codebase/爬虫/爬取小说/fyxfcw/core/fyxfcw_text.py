# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2511:39
# @Author  : 小符玩代码
# @Email   : 2737454073@qq.com
# @File    : fyxfcw_text.py
# @Software: PyCharm
import os
import random
import re
import time
import requests
from lxml import etree
import queue
import threading
from threading import Lock
from conf import Strings
from lib import module_fyxfcw

q = queue.Queue()
c = queue.Queue()

lock = Lock()
path_dir = None
title = None


class p_gets(threading.Thread):
    """生产者"""

    def __init__(self, daemon):
        super(p_gets, self).__init__(daemon=daemon)
        self.heads = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
            'referer': "urls",
        }
        self.__quit_p = False

    def terminate(self) -> object:
        """
        主动关闭
        """
        self.__quit_p = True

    def run(self) -> None:
        """死循环用来保持进程可用"""
        while True:
            if self.__quit_p:
                break
            url, tuple_text = q.get()
            self.pget(url, tuple_text)

    def pget(self, url, tuple_text):
        """生产者请求网页"""
        self.heads['referer'] = url
        response = requests.get(url, headers=self.heads)
        response_2 = requests.get(f'{url.split(".html")[0]}_2.html', headers=self.heads)
        if response.status_code != 200:
            self.heads[
                'cookie'] = 'fontFamily=null; fontColor=null; fontSize=null; bg=null; bookid=69815; booklist=%257B%2522BookId%2522%253A69815%252C%2522ChapterId%2522%253A4837883%252C%2522ChapterName%2522%253A%25221.%25u70BC%25u6C14%25u671F%25u8001%25u7956%2522%252C%2522BookName%2522%253A%2522%25u70BC%25u6C14%25u7EC3%25u4E86%25u4E09%25u5343%25u5E74%2522%252C%2522Author%2522%253A%2522%25u7CBE%25u88C5%25u6FC0%25u5149%25u96D5%25u523B%25u673A%2522%257D; Hm_lvt_120911993bc7847513828ff048914d67=1658719909,1658719945,1658720199; ASP.NET_SessionId=lh1n3wa2nst04yduwadykptz; Hm_lpvt_120911993bc7847513828ff048914d67=1658720295'

            self.pget(url, tuple_text)
            # 递归，当他报错的时候加上cookis，然后递归他有一个递的过程和一个归的过程，所以这里要用到else，不然他会多次put到消费者队列
        else:
            c.put((response.text, tuple_text, response_2.text))


class c_html(threading.Thread):
    """消费者"""

    def __init__(self, daemon):
        super(c_html, self).__init__(daemon=daemon)
        self.__quit_c = False

    def terminate(self):
        """
        主动关闭
        """
        self.__quit_c = True

    def run(self) -> None:
        while True:
            if self.__quit_c:
                break
            c_get = c.get()
            self.c_text(c_get)

    def c_text(self, c_get):
        """消费者解析"""
        resource, tuple_text, resource_2 = c_get
        html = etree.HTML(resource)
        html_2 = etree.HTML(resource_2)
        text_list = html.xpath('//*[@id="content"]//text()')[5:] + html_2.xpath('//*[@id="content"]//text()')[5:]
        # 加入线程锁，用于锁定线程保证数据安全
        with lock:
            ff = open(os.path.join(path_dir, f'{tuple_text[1]}-{tuple_text[0]}.txt'), 'w+', encoding='utf-8')
            for text in text_list:
                text = re.sub('[”“\r\n]\u3000', '', text.strip())
                if len(text)>0:
                    ff.write(text+'\n')
            else:
                ff.close()


def create_chapter(urls, num=1):
    """生成章节"""
    heads = {
        'user-agent': random.choice(Strings.USER_AGENT_LIST),
        'referer': urls,
    }
    response = requests.get(urls, headers=heads).text
    html = etree.HTML(response)
    global title
    if not title:
        title = html.xpath('/html/body/div[3]/div[1]/div/div/div[2]/div[1]/h1/text()')[0]
    li_list = html.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li')
    for li in li_list:
        text_href = 'https://www.fyxfcw.com' + li.xpath('./a/@href')[0]
        text_title = module_fyxfcw.character_text(li.xpath('./a/text()')[0])
        if not re.match(r'^https?:/{2}\w.+$|^http?:/{2}\w.+$', text_href):
            continue
        if all((text_href, text_title)):
            q.put((text_href, (text_title, num)))
            num += 1
    try:
        # if num >= 100:return None
        page = 'https://www.fyxfcw.com/' + html.xpath('/html/body/div[3]/div[2]/div/div[3]/span[3]/a/@href')[0]
        print(num)
        create_chapter(page, num)
    except Exception as exce:
        print(exce)


def create_dir(dir, types):
    """生成目录"""
    global path_dir
    path_dir = os.path.join(Strings.ARTICLES_DIR, types, dir)
    print(f'开始创建{path_dir}')
    if not os.path.exists(path_dir):
        # 递归创建
        os.makedirs(path_dir)


def create_threading():
    """生成进程"""
    p_list = []  # 生产者线程队列，用于下面关闭
    c_list = []  # 消费者线程队列，用于下面关闭
    for i in range(Strings.PRODUCER_THREADING_MAX):
        p_get = p_gets(True)
        p_get.name = f'producer{i}'
        p_get.start()
        p_list.append(p_get)

    for i in range(Strings.CONSUMER_THREADING_MAX):
        c_html1 = c_html(True)
        c_html1.name = f'consumer{i}'
        c_html1.start()
        c_list.append(c_html1)

    while True:
        time.sleep(32)
        print('生产者队列是否清空了', c.empty() and c.qsize() == 0)
        print('消费者队列是否清空了', q.empty() and q.qsize() == 0)
        print('是否都清空了', q.empty() and c.empty())
        if q.empty() and q.qsize() == 0:
            if c.empty() and c.qsize() == 0:
                for i in c_list:
                    i.terminate()
            for i in p_list:
                i.terminate()
        if q.empty() and c.empty():
            break


def main(url, types='玄幻奇幻'):
    """启动方法默认16线程"""
    create_chapter(url)
    create_dir(os.path.join(title, '章节'), types)
    print(f"开始爬取{title}")
    create_threading()
    print(f'结束进程{os.getpid()}')
    module_fyxfcw.sum_file(path_dir)


if __name__ == '__main__':
    # urls = "https://www.xxbiqudu.com/105_105194/"
    # urls = 'https://www.xxbiqudu.com/3_3492/'
    # urls = 'https://www.fyxfcw.com/book/637/'
    # urls = 'https://www.fyxfcw.com/book/613/'
    # urls = 'https://www.fyxfcw.com/book/74827/'
    # urls = 'https://www.fyxfcw.com/book/68833/'
    urls = 'https://www.fyxfcw.com/book/73623/'
    main(urls)
