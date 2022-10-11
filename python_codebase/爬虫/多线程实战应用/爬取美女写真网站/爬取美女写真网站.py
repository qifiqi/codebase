# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/18 17:05
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : 爬取美女写真网站.py
# @Software: PyCharm

"""
使用多进程的爬取

"""
import requests
from concurrent.futures import ThreadPoolExecutor
from faker import Faker
from lxml import etree
import random, time
import os

fa = Faker('zh_CN')
ua = [fa.chrome() for i in range(100)]
threa = ThreadPoolExecutor(max_workers=3)
img_threa = ThreadPoolExecutor()
root = os.getcwd()
os.mkdir(os.path.join(root, 'img'))


def get_id(url, header):
    resp = requests.get(url, headers=header)
    if resp.status_code != 200:
        header['cookie'] = '__51vcke__Jim81uWfjZQWoV7f=8dfe50c4-2634-5294-a2b3-69476ef05baa; ' \
                           '__51vuft__Jim81uWfjZQWoV7f=1655394000824; PHPSESSID=mq1m3fel9k620qi1j2ar7tc2hc; ' \
                           '__51uvsct__Jim81uWfjZQWoV7f=2; ' \
                           '__vtins__Jim81uWfjZQWoV7f=%7B%22sid%22%3A%20%2250b2a12d-e687-568f-a2ae-30415219bcb5%22' \
                           '%2C%20%22vd%22%3A%207%2C%20%22stt%22%3A%201424041%2C%20%22dr%22%3A%20177784%2C%20' \
                           '%22expires%22%3A%201655540337340%2C%20%22ct%22%3A%201655538537340%7D; ' \
                           'wordpress_logged_in_6996da195f5c2ad17afb59fea8ddf62a=asd%7C1656748151' \
                           '%7Cv9Z7c60mx2UQTZHmaTKyqxa9h5E2huRA5tfsntgqOvf' \
                           '%7Cc5b1c32dd51eda43e89caced7644e24ab7aad6a1833845c3d4d5a4d935cf14c5 '
        get_id(url, header)
        time.sleep(0.1)
    html = etree.HTML(resp.text)
    divs = html.xpath('//div[@class="col-lg-5ths col-lg-3 col-md-4 col-6"]')
    for div in divs:
        img_url = div.xpath('./div/div[1]/div/a/@href')[0]
        print(f"当前爬取到这个了{img_url}")
        threa.submit(get_img_url, (img_url, header))
        time.sleep(0.1)


def get_img_url(img_url, head):
    res = requests.get(url=img_url, headers=head)
    html = etree.HTML(res.text)
    imgs = html.xpath('//*[@id="gallery"]/figure/div/img')
    for img in imgs:
        img_url_path = img.xpath("./@src")[0].split('?')[0]
        img_threa.submit(xiazai_img, img_url_path)
        time.sleep(0.1)


def xiazai_img(img_path):
    res = requests.get(img_path)
    file_name = img_path.split('/')[-1]
    print(f'下载name:{file_name}，img——path:{img_path}')
    with open(f'./img/{file_name}', 'wb+') as img:
        img.write(res.content)
        img.close()


def main():
    for i in range(2, 50):
        header = {
            'user-agent': random.choice(ua),
            'referer': 'https://www.xtuge.com/page/%d' % (i - 1),
        }
        get_id(url='https://www.xtuge.com/page/%d' % i, header=header)
        print(f"第几页{i}地址{'https://www.xtuge.com/page/%d' % i}")
        time.sleep(0.1)



if __name__ == '__main__':
    print("开始运行")
    main()
