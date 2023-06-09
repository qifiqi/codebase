# -*- coding: utf-8 -*-
"""
Created on 2023-05-29 22:37:02
---------
@summary:
---------
@author: FQCj
"""

import feapder
from items import meishitxia_item


class MeishitianxiaspiderPull(feapder.Spider):
    # 自定义数据库，若项目中有setting.py文件，此自定义可删除
    # __custom_setting__ = dict(
    #     REDISDB_IP_PORTS="localhost:6379", REDISDB_USER_PASS="", REDISDB_DB=0
    # )

    # def start_requests(self):
    #     url = "https://home.meishichina.com/recipe-type.html"
    #     yield feapder.Request(url, method="GET")

    def download_midware(self, request):
        request.headers = {
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
            "sec-ch-ua-platform": "^\\^Windows^^"
        }

        return request

    def download_midware_info(self, request):
        request.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Referer": f"{request.items['pageAddress']}",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "sec-ch-ua": "^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^"
        }
        return request

    def parse(self, request, response):
        datas = request.datas
        for li in response.css("#J_list ul li"):
            item = meishitxia_item.MeishitxiaItem()
            item['secondaryLabel'] = datas['secondaryLabel']
            item['pageAddress'] = datas['pageAddress']
            item['firstLevelLabel'] = datas['firstLevelLabel']

            item['title'] = li.css("div.pic a::attr(title)").extract_first()
            item['item_href'] = li.css("div.pic a::attr(href)").extract_first()
            item['img_href'] = li.css("div.pic a img.imgLoad::attr(data-src)").extract_first()
            item['details'] = li.css('p.subcontent::text').extract_first()
            print(item)
            yield feapder.Request(
                url=item['item_href'],
                callback=self.parse_item,
                items=item,
                download_midware=self.download_midware_info,
                priority=200
            )
        try:
            next_href = response.css('div.ui-page-inner a')[-1].css("::attr(href)").extract_first()
            if next_href is not None:
                yield feapder.Request(
                    url=next_href,
                    callback=self.parse,
                    datas={
                        'secondaryLabel': datas['secondaryLabel'],
                        'firstLevelLabel': datas['firstLevelLabel'],
                        'pageAddress': next_href,
                    },
                    priority=300
                )
        except Exception as a:
            pass

    def parse_item(self, request, response):
        item = request.items
        item['html'] = response.css('div.space_left').extract_first()
        print(item)
        # yield item


if __name__ == "__main__":
    MeishitianxiaspiderPull(redis_key="meishitianxia:key", keep_alive=False, wait_lock=True,thread_count=1).start()
