# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/2/1115:48
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : main.py
__author__ = 'Small Fu'


import os
import time

import requests
from concurrent.futures import ThreadPoolExecutor
import queue
from tqdm import tqdm
from parsel import Selector

"""
https://www.bixiange.top/
"""

q = queue.Queue()
th = ThreadPoolExecutor(max_workers=32)

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33",
}

titles = "我真没想重生啊"
titles_text = '正文'


def put_list(url: str):
    head['Referer'] = url
    response = requests.get(url=url, headers=head)
    html = Selector(response.content.decode("gbk"))

    global titles
    titles = html.css("div.desc h1::text").get("").split("(")[0]

    if not os.path.exists(f'./{titles}'):
        os.makedirs(f"./{titles}/{titles_text}/")

    dd_list = html.css(".clearfix>li>a")

    for i, dd in enumerate(dd_list):
        path = "https://www.bixiange.top" + dd.css("::attr(href)").get("")
        q.put((i, path, titles_text))

    pass


def get_text(i, path, section):
    response = requests.get(url=path, headers=head)
    html = Selector(response.content.decode("gbk"))
    title = html.css(".article h1::text").get("")
    text_list = html.css("#mycontent ::text").getall()
    print(title)
    print(f"{title} 写入文件")
    if i is not None:
        with open(f'./{titles}/{section}/{i}_{title.strip()}.txt', 'w+', encoding='utf-8') as files:
            files.write(title + '\r\n')
            for text in text_list[:-2]:
                if len(text) < 2:
                    continue
                files.write(text.replace("\xa0", '').replace("\r", '')+"\n")
            else:
                files.write("\r\n")

    else:
        with open(f'./{titles}/{section}/{title}.txt', 'w+', encoding='utf-8') as files:
            files.write(title + '\r\n')
            for text in text_list[:-2]:
                if len(text) < 2:
                    continue
                files.write(text.replace("\xa0", '').replace("\r", '')+"\n")
            else:
                files.write("\r\n")

    print(f"{title} 写入完成")


def sum_text():
    print(f'./{titles}/ 合并中')
    dirs_title = os.listdir(f'./{titles}/{titles_text}')
    dirs_title = sorted(dirs_title, key=lambda x: int(x.split('_')[0]))
    file = open(f'./{titles}/{titles}.txt', 'w+', encoding="utf-8")
    for dir in tqdm(dirs_title):
        with open(f'./{titles}/{titles_text}/{dir}', 'r', encoding='utf-8') as ff:
            file.write(ff.read())
            ff.close()
    file.close()


def main(url):
    put_list(url)
    print(q.qsize())

    while q.qsize() > 0:
        i, path, title_text = q.get()
        th.submit(get_text, i, path, title_text)

    time.sleep(32)


def run():
    # url_path = "https://www.bixiange.top/dsyq/17688/"
    url_path = "https://www.powanjuan.cc/dsyq/16402/"
    # put_list(url_path)
    # get_text(1, "https://www.ddyueshu.com/12_12497/5886238.html", "《我真没想重生啊》正文")

    main(url_path)
    th.shutdown(wait=True)
    sum_text()


if __name__ == '__main__':
    run()
