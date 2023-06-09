# -*- coding: utf-8 -*-
"""
Created on 2023-05-28 12:58:54
---------
@summary:
---------
@author: FQCj
"""

import feapder
from feapder.db.mysqldb import MysqlDB
from items import xiachufangitem_item


class Xiachufangitem(feapder.Spider):
    # 自定义数据库，若项目中有setting.py文件，此自定义可删除
    # __custom_setting__ = dict(
    #     REDISDB_IP_PORTS="localhost:6379", REDISDB_USER_PASS="", REDISDB_DB=0
    # )

    def __init__(
            self,
            redis_key=None,
            min_task_count=1,
            check_task_interval=5,
            thread_count=None,
            begin_callback=None,
            end_callback=None,
            delete_keys=(),
            keep_alive=None,
            auto_start_requests=None,
            batch_interval=0,
            wait_lock=True,
            **kwargs
    ):
        super().__init__(redis_key, min_task_count, check_task_interval, thread_count, begin_callback, end_callback,
                         delete_keys, keep_alive, auto_start_requests, batch_interval, wait_lock, **kwargs)
        self.db = None
        self.data = None

    def start_callback(self):
        self.db = MysqlDB()
        self.data = self.db.find(sql="SELECT * FROM xiachufanglabel;", to_json=True)

    def start_requests(self):
        for i in self.data:
            print(i['dir_url'])
            yield feapder.Request(url=i['dir_url'], aa_data=i)
            self.db.update(f'UPDATE xiachufanglabel SET state=1 WHERE id={i["id"]}')


    def download_midware_info(self, request):
        request.headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Referer": request.aa_data["Referer"],
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": "^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^"
        }
        request.cookies = {
            "bid": "M53qFyWj",
            "sensorsdata2015jssdkcross": "^%^7B^%^22distinct_id^%^22^%^3A^%^221885db942c650e-0d570fbe22329e-26031a51-1327104-1885db942c7514^%^22^%^2C^%^22^%^24device_id^%^22^%^3A^%^221885db942c650e-0d570fbe22329e-26031a51-1327104-1885db942c7514^%^22^%^2C^%^22props^%^22^%^3A^%^7B^%^22^%^24latest_referrer^%^22^%^3A^%^22^%^22^%^2C^%^22^%^24latest_referrer_host^%^22^%^3A^%^22^%^22^%^2C^%^22^%^24latest_traffic_source_type^%^22^%^3A^%^22^%^E7^%^9B^%^B4^%^E6^%^8E^%^A5^%^E6^%^B5^%^81^%^E9^%^87^%^8F^%^22^%^2C^%^22^%^24latest_search_keyword^%^22^%^3A^%^22^%^E6^%^9C^%^AA^%^E5^%^8F^%^96^%^E5^%^88^%^B0^%^E5^%^80^%^BC_^%^E7^%^9B^%^B4^%^E6^%^8E^%^A5^%^E6^%^89^%^93^%^E5^%^BC^%^80^%^22^%^7D^%^7D",
            "__bid_n": "1885db943663367b564207",
            "Hm_lvt_ecd4feb5c351cc02583045a5813b5142": "1685199603",
            "__utmc": "177678124",
            "__utmz": "177678124.1685199603.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none)",
            "__gads": "ID=6a0c0734819168c5-22ef44c7dae000b2:T=1685199609:RT=1685202457:S=ALNI_MYrmzg-IPL_VEnrMueZ0s3swehEyQ",
            "__gpi": "UID=00000c39ef505b69:T=1685199609:RT=1685202457:S=ALNI_Mb46elmo8WfUb83O-ZYImGXBuRjFw",
            "__utma": "177678124.2007361443.1685199603.1685202449.1685251595.3",
            "__utmt": "1",
            "FPTOKEN": "+oQiG1r5KvHHp9ZwY0qA5WRW4aaT0l122MUraBIrwkKK+5dLfzFcFXSF7XiOZuJ987PyFdR0pxQD1ASZbP5f8/KqTlWOIMrdmeMddd6Lhs3i+9PvhI3rvUKIh6LrKy9JU8VbXVRMrGEhnaB93cc2uXWcrtt1CwO4IdV5VSIGpeJlrc8CGK1dWZCrRqtkur1p88m2E7X3DaFSWxX98+cPXg6Eb5EsUDSN4DzsSHL6JQNietSwedHUZcRZPdfnOexhqXBZsd1QFOPDO6HVAjMVcsH4ro9X/Y3pABuTP1HXsYY307zjLWEFrYkkqkLXd2iVKtZgzGIPl7qlqLrXQGBX2Dqw0cTZxwug1xoM8n64CNq1MkeDA1/oX2bMFdZkivQCxd8U+CBCIOxJtrOnU+pHtQ==^|Ig2K0owXx9QlrtufPWlizQrF7Q/h73kLMzqjJ8UA5oo=^|10^|b679388fa446c0e200af36c5a8a6fd82",
            "__utmb": "177678124.2.10.1685251595",
            "Hm_lpvt_ecd4feb5c351cc02583045a5813b5142": "1685251608"
        }
        return request

    def parse(self, request, response):
        aa_data = request.aa_data
        for li in response.css('div.normal-recipe-list>ul.list>li'):
            aa_data['name'] = li.css("p.name a::text").extract_first().strip()
            item_url = li.css("p.name a::attr(href)").extract_first()
            item = xiachufangitem_item.XiachufangitemItem()
            aa_data = request.aa_data
            item["firstLevelLabel"] = aa_data["firstLevelLabel"]
            item["secondaryLabel"] = aa_data["secondaryLabel"]
            item["item_url"] = item_url + 'async_recipe_dishes/'
            item["title"] = aa_data["name"]
            item["htmlText"] = ''
            yield item
        next = response.css("a.next::attr(href)").extract_first()
        if next:
            yield feapder.Request(url=next, aa_data=aa_data,callback=self.parse)



if __name__ == "__main__":
    Xiachufangitem(redis_key="xiachufang:key", thread_count=12).start()
