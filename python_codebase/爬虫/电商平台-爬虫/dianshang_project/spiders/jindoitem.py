# -*- coding: utf-8 -*-
"""
Created on 2023-06-05 13:19:45
---------
@summary:
---------
@author: FQCj
"""
import csv
import json
import time

import feapder
from urllib import parse


class Jindoitem(feapder.AirSpider):
    def __init__(self, thread_count=None):
        super().__init__(thread_count)
        self.csv_file = None
        self.files = None

    def aa(self, i, repeat_count=0):
        if i > 1:
            s = (i - 1) * 30 - 5 + 1 + repeat_count
        else:
            s = (i - 1) * 30 + 1
        return s

    def start_requests(self):

        for i in range(1, 21, 2):
            s = self.aa(i)
            if i % 2 == 0:
                continue
            else:
                url = f'https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=8858151673f941e9b1a4d2c7214b2b52&page={i}&s={s}&click=0'

            time.sleep(1)
            # a = "&".join([k+'='+str(v) for k,v in params.items()])
            yield feapder.Request(url, method="GET", a_data={"page": i, "url": url})
            break

    def start_callback(self):
        self.files = open("./jindoCsv.csv", "w+", encoding="utf-8", newline="")
        self.csv_file = csv.writer(self.files)

    def end_callback(self):
        self.files.close()

    def download_midware(self, request):
        request.headers = {
            "authority": "search.jd.com",
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": request.a_data["url"],
            "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37",
            "x-requested-with": "XMLHttpRequest"
        }
        return request

    def parse(self, request, response):
        for li in response.css("#J_goodsList>ul>li"):
            item = {}
            if li.css("::attr(ware-type)").extract_first() == "0":
                continue
            item['data-sku'] = li.css('::attr(data-sku)').extract_first()
            item["p-name"] = " ".join(li.css("div.p-name em ::text").extract())
            item["a_href"] = li.css("div.p-name>a::attr(href)").extract_first()
            item["flagsClk"] = li.css("div.p-name>a::attr(onclick)").extract_first()
            item["storeLink"] = li.css("span.J_im_icon>a::attr(href)").extract_first()
            item["storetitle"] = li.css("span.J_im_icon>a::attr(title)").extract_first()
            self.csv_file.writerow([v for v in item.values()])
            print(item)
        a_da = request.a_data

        if a_da['page'] % 2 != 0:
            log_id = response.css("script::text").extract_first().split("log_id")[1].split(":'")[1].split("',")[0]
            i = int(a_da['page']) + 1
            s = self.aa(i, 0)
            if i == 2:
                s = self.aa(i, 1)

            url = f'https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=8858151673f941e9b1a4d2c7214b2b52&page={i}&s={s}&scrolling=y&log_id={log_id}&tpl=3_M&isList=0&show_items='
            time.sleep(1)
            yield feapder.Request(url, method="GET", a_data={"page": i, "url": url})


if __name__ == "__main__":
    Jindoitem().start()
