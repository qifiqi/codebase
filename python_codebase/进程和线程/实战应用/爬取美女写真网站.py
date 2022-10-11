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
threa = ThreadPoolExecutor(max_workers=1)
img_threa = ThreadPoolExecutor(max_workers=30)
root = os.getcwd()
if not os.path.exists('./img'):
    os.mkdir(os.path.join(root, 'img'))



def get_id(url, header):
    resp = requests.get(url, headers=header)
    if resp.status_code != 200:
        header['cookie'] ='__51uvsct__Jim81uWfjZQWoV7f=1; __51vcke__Jim81uWfjZQWoV7f=ae626532-ca17-5eb6-aeeb-22fdfe91b9d5; __51vuft__Jim81uWfjZQWoV7f=1661259685583; PHPSESSID=47jddu0947pv1pua4v45accs18; Hm_lvt_14111874ee6bee7bc3accda44e91a023=1662650368; Hm_lpvt_14111874ee6bee7bc3accda44e91a023=1662650374'
        get_id(url, header)
        time.sleep(0.1)
    html = etree.HTML(resp.text)
    divs = html.xpath('//div[@class="col-lg-5ths col-lg-3 col-md-4 col-6"]')
    for div in divs:
        img_url = div.xpath('./div/div[1]/div/a/@href')[0]
        print(f"当前爬取到这个了{img_url}")
        threa.submit(get_img_url, img_url, header)


def get_img_url(img_url, head):
    res = requests.get(url=img_url, headers=head)
    html = etree.HTML(res.text)

    imgs = html.xpath('//*[@id="gallery"]/figure/div/img')
    for img in imgs:
        img_url_path = img.xpath("./@src")[0].split('?')[0]
        print(img_url_path)
        img_threa.submit(xiazai_img, img_url_path)
        return ''


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
    # xiazai_img('https://i5.imm133.xyz/wp-content/uploads/2020/10/2020102112125927481.jpg')