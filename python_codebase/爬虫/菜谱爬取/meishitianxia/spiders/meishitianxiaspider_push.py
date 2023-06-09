# -*- coding: utf-8 -*-
"""
Created on 2023-05-29 22:22:57
---------
@summary:
---------
@author: FQCj
"""

import feapder
import requests
from parsel import selector
from feapder import ArgumentParser
from items import meishitxia_item

class MeishitianxiaspiderPush(feapder.Spider):
    # 自定义数据库，若项目中有setting.py文件，此自定义可删除
    # __custom_setting__ = dict(
    #     REDISDB_IP_PORTS="localhost:6379", REDISDB_USER_PASS="", REDISDB_DB=0
    # )

    def start_requests(self):
        url = "https://home.meishichina.com/recipe-type.html"
        response = requests.get(url, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "sec-ch-ua": "^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
        }).text
        response = selector.Selector(response)
        for div in response.css('div.category_box>div'):
            name = div.css('h3::text').extract_first()
            for li in div.css("ul>li"):
                datas = {}
                datas['secondaryLabel'] = li.css("a::text").extract_first()
                datas['pageAddress'] = li.css("a::attr(href)").extract_first()
                datas['firstLevelLabel'] = name
                yield feapder.Request(
                    url=datas['pageAddress'],
                    callback=meishitianxiaspider_pull.MeishitianxiaspiderPull.parse,
                    datas=datas,
                )

    def parse(self, request, response):
        # 提取网站title
        print(response.xpath("//title/text()").extract_first())
        # 提取网站描述
        print(response.xpath("//meta[@name='description']/@content").extract_first())
        print("网站地址: ", response.url)


if __name__ == "__main__":
    MeishitianxiaspiderPush(redis_key="meishitianxia:key", thread_count=1).start_monitor_task()
