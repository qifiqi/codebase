# -*- coding: utf-8 -*-
"""
Created on 2023-05-27 23:17:22
---------
@summary:
---------
@author: FQCj
"""

import feapder
from items import xiachufanglabel_item

class XiachufangUrl(feapder.AirSpider):


    def start_requests(self):
        url = "https://www.xiachufang.com/category/40071/"
        params = {
            "page": "2"
        }
        yield feapder.Request(url, params=params, method="GET", callback=self.parse)

    def download_midware(self, request):
        request.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Referer": "https://www.xiachufang.com/category/40071/",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "sec-ch-ua": "^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^"
        }
        request.cookies = {
            "bid": "M53qFyWj",
            "sajssdk_2015_cross_new_user": "1",
            "sensorsdata2015jssdkcross": "^%^7B^%^22distinct_id^%^22^%^3A^%^221885db942c650e-0d570fbe22329e-26031a51-1327104-1885db942c7514^%^22^%^2C^%^22^%^24device_id^%^22^%^3A^%^221885db942c650e-0d570fbe22329e-26031a51-1327104-1885db942c7514^%^22^%^2C^%^22props^%^22^%^3A^%^7B^%^22^%^24latest_referrer^%^22^%^3A^%^22^%^22^%^2C^%^22^%^24latest_referrer_host^%^22^%^3A^%^22^%^22^%^2C^%^22^%^24latest_traffic_source_type^%^22^%^3A^%^22^%^E7^%^9B^%^B4^%^E6^%^8E^%^A5^%^E6^%^B5^%^81^%^E9^%^87^%^8F^%^22^%^2C^%^22^%^24latest_search_keyword^%^22^%^3A^%^22^%^E6^%^9C^%^AA^%^E5^%^8F^%^96^%^E5^%^88^%^B0^%^E5^%^80^%^BC_^%^E7^%^9B^%^B4^%^E6^%^8E^%^A5^%^E6^%^89^%^93^%^E5^%^BC^%^80^%^22^%^7D^%^7D",
            "__bid_n": "1885db943663367b564207",
            "Hm_lvt_ecd4feb5c351cc02583045a5813b5142": "1685199603",
            "__utmc": "177678124",
            "__utmz": "177678124.1685199603.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none)",
            "FPTOKEN": "iYgvj8bBRpHHOo0kWExqnyHWg3S6IG6B6/uY+RIHbiA0NKbk+KNETw1D9tBk+5cwkrkTSVQ7MLpGp+xTaaLPPXSFbaQ6YRg+wNEuhFrEY+tz3v6dHK8PUY3W8e61KVoecJLtWCOPRiRNkTuKXV1EoWJvJTxSSs59SxvPpOxvSQLlnBcqjxfibpWfeVfvk1C7FRdIdWC6zo9SO7crETiITFHMb2EdtfvfbmTS7QYZdx6QC87Ru7bkAPdMwYwS4C20cO9uB6xy9zhvyTpjXbS5oyhNu3nw3yOvpP3U9q27QfKX897ZR9BLmYIdcmb+figpQSzzQRlHHrsW2/5V7ZEbwwnbbNVg3SxvEtjuafvaMJgG5opnrdFnTl60ItDKugj921SZPDkmXaHjD/ZTC2QaqQ==^|OIdx105zxtzKRfWMpfcUWTP/uVqrrNgcVrryFabFGag=^|10^|8e83fab8d76558031e52037b29066fb2",
            "__utma": "177678124.2007361443.1685199603.1685199603.1685202449.2",
            "__utmt": "1",
            "__gads": "ID=6a0c0734819168c5-22ef44c7dae000b2:T=1685199609:RT=1685202457:S=ALNI_MYrmzg-IPL_VEnrMueZ0s3swehEyQ",
            "__gpi": "UID=00000c39ef505b69:T=1685199609:RT=1685202457:S=ALNI_Mb46elmo8WfUb83O-ZYImGXBuRjFw",
            "Hm_lpvt_ecd4feb5c351cc02583045a5813b5142": "1685202459",
            "__utmb": "177678124.2.10.1685202449"
        }
        return request

    def parse(self, request, response):
        for div_li in response.css("div.category-left-tree>ul.plain>li"):
            firstLevelLabel = div_li.css("p.name::text").extract_first()
            for li in div_li.css("ul.level2>li"):
                item = xiachufanglabel_item.XiachufanglabelItem()
                secondaryLabel = li.css("a::text").extract_first().strip()
                _href = li.css("a::attr(href)").extract_first()
                item["firstLevelLabel"] = firstLevelLabel
                item["secondaryLabel"] = secondaryLabel
                item["dir_url"] = _href
                yield item


if __name__ == "__main__":
    XiachufangUrl().start()
