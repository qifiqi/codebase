# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/1615:45
# @Author  : 小符玩代码
# @Email   : 2737454073@qq.com
# @File    : xxbiqudu.py
# @Software: PyCharm
import os
import re
import sys
import time

import faker
import requests
from lxml import etree
import queue
import threading
from threading import Lock

from 爬取笔趣阁.sum_text import sum_file

q = queue.Queue()
c = queue.Queue()

lock = Lock()
path_dir = None
title = None


class p_gets(threading.Thread):
    """生产者"""

    def __init__(self, urls):
        self.fa = faker.Faker('zh_CN')
        super().__init__(daemon=True)
        self.heads = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
            'referer': urls,
        }
        self.__quit_p = False

    def terminate(self):
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
        self.heads['user-agent'] = self.fa.chrome()
        response = requests.get(url, headers=self.heads)
        if response.status_code != 200:
            self.heads[
                'cookie'] = 'ckAC=1; Hm_lvt_ac7b23f05f611c864643cf046915ae1f=1657957257; __gads=ID=6f4622285951846f-225c4d1436d500a0:T=1657957259:RT=1657957259:S=ALNI_MYJJoO_Vd3UF-9rc9HoehnETXbiww; __gpi=UID=000007c2fd695e26:T=1657957259:RT=1657957259:S=ALNI_MZyCoaV_N2F4m0BLcs1zX47p7b3KA; ras=2; width=85%25; Hm_lpvt_ac7b23f05f611c864643cf046915ae1f=1657957973'

            self.pget(url, tuple_text)
            # 递归，当他报错的时候加上cookis，然后递归他有一个递的过程和一个归的过程，所以这里要用到else，不然他会多次put到消费者队列
        else:
            c.put((response.text, tuple_text))


class c_html(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)

        self.__quit_p = False

    def terminate(self):
        self.__quit_p = True

    def run(self) -> None:
        while True:
            if self.__quit_p:
                break
            c_get = c.get()
            self.c_text(c_get)

    def c_text(self, c_get):
        """消费者解析"""
        resource, tuple_text = c_get
        html = etree.HTML(resource)
        text_list = html.xpath('//*[@id="content"]//text()')
        # 加入线程锁，用于锁定线程保证数据安全
        with lock:
            ff = open(os.path.join(path_dir, f'{tuple_text[1]}-{tuple_text[0]}.txt'), 'w+', encoding='utf-8')
            for text in text_list:
                ff.write(str(text).strip() + '\n')
            else:
                ff.close()
        print(tuple_text[0] + 'ok')


def main(urls):
    """生成章节"""
    heads = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
        'referer': urls,
    }
    response = requests.get(urls, headers=heads).text
    html = etree.HTML(response)
    global title
    title = html.xpath('//*[@id="info"]/h1/text()')[0]
    dt_list = html.xpath('//div[@id="list"]/dl//dd')[10:]
    for num, dt in enumerate(dt_list):
        text_href = dt.xpath('./a/@href')[0]
        text_title = dt.xpath('./a/text()')[0]
        if not re.match(r'^https?:/{2}\w.+$|^http?:/{2}\w.+$', text_href):
            continue
        if all((text_href, text_title)):
            q.put((text_href, (text_title, num)))


def create_dir(dir):
    """生成目录"""
    global path_dir
    path_dir = os.path.join(os.path.dirname(__file__), dir)

    if not os.path.exists(path_dir):
        # 递归创建
        os.makedirs(path_dir)


def create_threading(urls):
    """生成进程"""
    p_list = []  # 生产者线程队列，用于下面join
    c_list = []  # 消费者线程队列，用于下面join
    for i in range(16):
        p = p_gets(urls)
        p.name = f'producer{i}'
        p.start()
        p_list.append(p)

    for i in range(3):
        c_html1 = c_html()
        c_html1.name = f'consumer{i}'
        c_html1.start()
        c_list.append(c_html1)

    for i in p_list:
        i.join()

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


if __name__ == '__main__':
    # urls = "https://www.xxbiqudu.com/105_105194/"
    # urls = 'https://www.xxbiqudu.com/3_3492/'
    urls = 'https://www.xxbiqudu.com/9_9151/'
    main(urls)
    create_dir(title + '/章节/')
    create_threading(urls)
    print('结束')
    sum_file(path_dir)
    sys.exit()
