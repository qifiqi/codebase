# -*- coding: utf-8 -*-
"""
Created on 2023-05-28 19:30:45
---------
@summary:
---------
@author: FQCj
"""
import random

import feapder
from items import meishitxia_item


class Xiachufangitem(feapder.AirSpider):

    def start_requests(self):
        url = "https://home.meishichina.com/recipe-type.html"
        yield feapder.Request(url, method="GET", priority=100)

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
        for div in response.css('div.category_box>div'):
            name = div.css('h3::text').extract_first()
            for li in div.css("ul>li"):
                datas = {}
                datas['secondaryLabel'] = li.css("a::text").extract_first()
                datas['pageAddress'] = li.css("a::attr(href)").extract_first()
                datas['firstLevelLabel'] = name
                yield feapder.Request(
                    url=datas['pageAddress'],
                    callback=self.parse_info,
                    datas=datas,
                    use_session=True,
                    priority=200

                )
            #     break
            # break

    def parse_info(self, request, response):
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
                    callback=self.parse_info,
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
        yield item


if __name__ == "__main__":
    Xiachufangitem().start()
