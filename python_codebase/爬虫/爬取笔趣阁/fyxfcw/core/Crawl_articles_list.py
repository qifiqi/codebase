# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2723:31
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : Crawl_articles_list.py
# @Software: PyCharm
__author__ = 'Small Fu'

import json

import requests
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor
from lxml import etree

from conf import Strings


class ArticlesListThread(Thread):
    def __init__(self, types, types_num=1, page=1):
        super().__init__()
        self.types = types
        self.lock = Lock()
        self.page_all = 0
        self.url = f'https://www.fyxfcw.com/ksl/{types_num}/{page}.html'
        self.heads = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
            'referer': f'https://www.fyxfcw.com/ksl/{types_num}/{page}.html',
        }
        self.types_num = types_num
        self.Th = ThreadPoolExecutor(max_workers=Strings.THREADPOOLEXECUTOR_MAX)
        self.file = open(f'./{types}.json', 'w+', encoding='utf-8')

    def run(self) -> None:
        print(f'开始爬取{self.types}')
        response = requests.get(url=self.url, headers=self.heads).text
        html = etree.HTML(response)
        # 获取总共多少页
        self.page_all = html.xpath('/html/body/div[3]/div[2]/div[1]/ul[2]/li[1]/span/text()[2]')[0].split('/')[-1]
        for page in range(2, int(self.page_all) + 1):
            url = f'https://www.fyxfcw.com/ksl/{self.types_num}/{page}.html'
            self.Th.submit(self.path_list, url)

    def path_list(self, url):
        print(url)
        self.heads['referer'] = url
        response = requests.get(url, self.heads).text
        html = etree.HTML(response)
        li_list = html.xpath('/html/body/div[3]/div[2]/div[1]/ul[1]/li')
        for li in li_list:
            text_href = li.xpath('./span[@class="s2"]/a/@href')[0]
            text = li.xpath('./span[@class="s2"]/a/text()')[0]
            with self.lock:
                self.file.write(
                    json.dumps(
                        {
                            'text_href': text_href,
                            'text': text
                        }
                        , ensure_ascii=False
                    )
                )


def articles_list():
    pro_list = []
    for types_num in range(1, 8):
        types = Strings.ARTICLES_TYPE_DICT[f"{types_num}"]
        pro = ArticlesListThread(types, types_num)
        pro.name = types
        pro.start()
        pro_list.append(pro)

    for i in pro_list:
        i.join()


if __name__ == '__main__':
    articles_list()
