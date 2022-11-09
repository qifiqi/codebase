# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/25 14:34
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : kuai_ip.py
# @Software: PyCharm
import json
import random
import time

import requests
import queue
from threading import Thread
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

kuai_generator = ThreadPoolExecutor(max_workers=3)  # 生产者
ip_queue = queue.Queue()  # 设置队列

ip_ = []

def generators(url):
    header = {
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
    }

    response = requests.get(url=url, headers=header)
    print(response.status_code)
    html = etree.HTML(response.text)
    tr_list = html.xpath('//div[@id="list"]/table/tbody/tr')
    for tr in tr_list:
        ip = tr.xpath('./td[1]/text()')[0]
        port = tr.xpath('./td[2]/text()')[0]
        cd = tr.xpath('./td[3]/text()')[0]
        lx = tr.xpath('./td[4]/text()')[0]
        ips = ip + ":" + port
        times = tr.xpath('./td[6]/text()')[0].replace('秒', '')

        if float(times) >= 3 and cd == '高匿名':
            ip_queue.put((
                ips, lx, ip
            ))


def consumers():
    while True:
        if ip_queue.empty():
            break
        aa = ip_queue.get()
        jc_ip_url = 'https://httpbin.org/ip'
        proxies = {
            'http': aa[0],
            'https': aa[0]
        }
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'
        }
        try:
            response = requests.get(url=jc_ip_url, headers=header, proxies=proxies, timeout=7).json()
            ip = response['origin']
            if ip == aa[2]:
                ip_.append(
                    proxies
                )
                print(ip_)
        except Exception as aa:
            print(aa)
        ip_queue.task_done()


if __name__ == '__main__':
    url_list = [f'https://free.kuaidaili.com/free/inha/{i}/' for i in range(1, 200)]

    for url in url_list:  # 设置生产者
        kuai_generator.submit(generators, url)

    consumer_list = [f'p{i}' for i in range(20)]
    consumer = []

    time.sleep(2)
    for i in consumer_list:
        aa = Thread(target=consumers, name=i)
        aa.start()
        consumer.append(aa)

    for i in consumer:
        i.join()

    with open('./ip.json', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(ip_))
        f.close()
