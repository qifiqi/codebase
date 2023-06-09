# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/5/2611:09
# @File    : demo1.py
import csv

import feapder


class AirSpiderDemo(feapder.AirSpider):
    def start_requests(self):
        url = "https://data.weibo.com/index/ajax/newindex/getchartdata"
        data = {
            "wid": "1091324264913",
            "dateGroup": "3month"
        }
        yield feapder.Request(url, data=data, method="POST")

    def download_midware(self, request):
        request.headers = {
            "authority": "data.weibo.com",
            "accept": "application/json",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://data.weibo.com",
            "pragma": "no-cache",
            "referer": "https://data.weibo.com/index/newindex?visit_type=trend&wid=1091324264913",
            "sec-ch-ua": "^\\^Microsoft",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "^\\^Android^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36 Edg/113.0.1774.50",
            "x-requested-with": "XMLHttpRequest"
        }
        request.cookies = {
            "SINAGLOBAL": "1176584170351.014.1683694614306",
            "SUB": "_2A25JX1R-DeRhGeBL6FQT9CzIzz6IHXVqoHw2rDV8PUJbkNAGLUzVkW1NRwq7cSf6qCKAyIsVUQ1ULC7jGF_frBWl",
            "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WFygYPanwb1DNckiJ32h9U-5NHD95QcSKeceoBEShBEWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSo-0SozXeoBXentt",
            "ULV": "1684897997227:2:2:1:3621145919557.649.1684897997215:1683694614308"
        }
        return request

    def parse(self, request, response):
        json_data = response.json
        print(json_data)
        _csv = open("./demo1.csv", "a+", encoding="utf-8",newline="")
        demo_csv = csv.writer(_csv)
        demo_csv.writerow(['关键字', '日期', '指数值'])
        for x, y in zip(json_data["data"][0]["trend"]["x"], json_data["data"][0]["trend"]["s"]):
            demo_csv.writerow([
                json_data["data"][0]["trend"]["name"],
                x, y
            ])

        _csv.close()

if __name__ == "__main__":
    AirSpiderDemo(thread_count=1).start()
