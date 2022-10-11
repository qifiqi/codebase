# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/29 17:03
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : libvio.py
# @Software: PyCharm
import json
import re
import sys

import requests
from urllib import parse
from lxml import etree
from tqdm import tqdm

session = requests.Session()


def getdy(title):
    ss_url = f'https://www.libvio.me/search/-------------.html?wd={parse.quote(title)}&submit='
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
        'Referer': 'https://www.libvio.me/',
    }
    response = session.get(ss_url, headers=header, timeout=5).text
    html = etree.HTML(response)
    try:
        aa = html.xpath(f'//a[@title="{title}"]/@href')[0]
    except Exception as aa:
        print('电影不存在')
    getdy_url(url=aa, title=title)


def getdy_url(url, title):
    num = str(url).split('/')[-1].split('.')[0]
    path = f'/play/{num}-1-1.html'
    url = f'https://www.libvio.me/play/{num}-1-1.html'
    header = {
        'path': path,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
    }
    response = requests.get(url=url, headers=header).text
    html = etree.HTML(response)
    aa = html.xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/div[1]/script[1]/text()')[0]
    aa = re.findall('\{(.*?)\}', aa)[0]
    js = json.loads("{" + aa + "}")
    header = {
        'referer': 'https://www.libvio.me/',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'path': f'/lb.php?url={js["url"]}&next={path}&id={js["id"]}&nid={js["nid"]}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
    }
    url = f'https://sh-data-s01.chinaeast2.cloudapp.chinacloudapi.cn/lb.php?url={js["url"]}&next={path}&id={js["id"]}&nid={js["nid"]}'
    response = session.get(url, headers=header).text
    urlpath = re.findall('var urls = \'(.*?.mp4)\'', response)[0]
    print('电影下载地址：\n', urlpath)
    xz(urlpath, title=title)


def xz(url, title):
    response = requests.get(url, stream=True)  # 采用流处理传输输入
    # 查看数据大小
    data_sice = int(response.headers['Content-Length'])
    print(data_sice)
    rr = tqdm(
        total=data_sice,
        desc=f'下载{title}',
        unit='mb',
        unit_scale=True,
        colour='Pink'
    )
    with open(f'./{title}.mp4', 'wb+') as ff:
        for i in response.iter_content(1024 * 1024):
            rr.update(len(i))
            ff.write(i)
        ff.close()


def main():
    title = input('请输入你要下载的视频')
    if len(title) <= 0:
        sys.exit()
    getdy(title=title)


if __name__ == '__main__':
    main()
