# -*- coding: utf-8 -*-
# All Rights Reserved
# @Time    : 2023/9/2223:15
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : dow_day.py
__author__ = 'Small Fu'

import requests
from parsel import Selector
from lxml import etree
import json
import os
import time

import aligo
import subprocess

from aligo.types import EMailConfig

# aligo_clise = aligo.Aligo(
#     email=EMailConfig(
#         email='2737454073@qq.com',
#         host='smtp.163.com',
#         port=465,
#         user='xiaofu_base@163.com',
#         password='OYSHQLSAGFDLZXIF',
#     )
# )


# f_aa = open("./aa.txt", 'a+', encoding="utf-8")


def dow(url, name, id):
    print(id,name)
    this_file_dir_path = os.path.abspath(os.path.dirname(__file__))
    aa = subprocess.run(f"sudo ./ffmpeg-6.0-amd64-static/ffmpeg -i {url} {name}.mp4", shell=True, stdout=subprocess.PIPE, cwd=this_file_dir_path)


def pull_aligo(path):
    aligo_clise.upload_file(
        file_path=path,
        parent_file_id='650c5752bd25ade7c4a349eca9d0cafbe03ed1de',
        name=path.split('/')[-1],
    )


def main(item):
    data = json.loads(item)
    id = data["data-video-id"]
    m3u8 = data["mp4_url_m3u8"]
    title = data["data-video-title"]
    dow(url=m3u8, name=title, id=id)
    pull_aligo(path=f"{id}.mp4")
    time.sleep(5)
    os.remove(f"{id}.mp4")
    print(f"{id}.mp4 删除")

file_t = open('./aa.json','a',encoding='utf-8')
import json
def m3u8():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }

    url = "https://vip.aqdk229.com:2096/videos/index/1"
    import urllib.parse

    response = requests.get(url, headers=headers)
    # sel = Selector(text=response.text)
    sel = etree.HTML(text=response.text)
    aa = sel.xpath('//*[@id="crypt_html_js"]/text()')
    if not aa:
        aa = aa.split("html = '")[-1].strip("';")
        aa = ''.join(list(aa)[::-1])
        aa = urllib.parse.unquote(aa)
        sel = Selector(aa)
    for item in sel.xpath('//div[@node-type="latest-video"]/div[not(contains(@class,"video-item-ads"))]'):
        d = {}
        d['data-video-id'] = item.xpath("./div/@data-video-id").get('')
        d['data-video-title'] = item.xpath(".//a[@class='thumbnail-cover-link']/@alt").get('')
        href = 'https://vip.aqdk229.com:2096' + item.xpath(".//a[@class='thumbnail-cover-link']/@href").get('')
        d['data-video-href'] = href
        d['data-video-img'] = item.xpath('.//img/@src').get('')
        d['desc'] = " ".join([i.strip() for i in item.xpath('.//div[@class="video-metadata-line"]//text()').getall()])

        aa = requests.get(href, headers=headers)
        aa = Selector(aa.text)
        aa = aa.css('#crypt_html_js::text').get('')
        if not aa:
            aa = aa.split("html = '")[-1].strip("';")
            aa = Selector(urllib.parse.unquote(''.join(list(aa)[::-1])))
        mp4_url_m3u8 = aa.xpath('/html/body/script[8]/text()').get().split('url: "')[-1].split('",')[0]
        bq = aa.xpath('/html/body/section/div[2]/div[2]/div[4]/div/div[4]/p/a/button/text()').getall()
        d['mp4_url_m3u8'] = mp4_url_m3u8
        d['bq'] = bq
        print(d)
        file_t.write(json.dumps(d,ensure_ascii=False)+'\n')
        main(json.dumps(d,ensure_ascii=False))

if __name__ == '__main__':
    import schedule
    schedule.every().day.at("01:30").do(m3u8)
    while True:
        schedule.run_pending()
        print('目前为：{}'.format(time.strftime('%Y-%m-%d %H:%M')))
        time.sleep(60 * 60)
    # m3u8()

