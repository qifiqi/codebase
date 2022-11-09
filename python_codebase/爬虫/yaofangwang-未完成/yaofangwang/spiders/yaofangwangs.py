import json

import requests
import scrapy
from yaofangwang.items import YaofangwangItem
from scrapy.selector import Selector


class YaofangwangsSpider(scrapy.Spider):
    name = 'yaofangwangs'
    # allowed_domains = ['yaofangwang.com']
    # start_urls = [f"https://www.yaofangwang.com/catalog-1/p{i}/" for i in range(1,1156)]
    start_urls = ["https://www.yaofangwang.com/catalog-1/p1/"]

    def parse(self, response):
        li_list = response.css("ul.goodlist li")
        path = response.css("a.next::attr(href)").extract_first()
        if path is not None:
            next_path = "https://www.yaofangwang.com" + path
            yield scrapy.Request(
                url=next_path,
                callback=self.parse,
                dont_filter=True
            )

        rel_list = []
        for li in li_list:
            rel = li.css("div.info::attr(rel)").extract_first()
            rel_list.append(rel)

        rel = "%2C".join(rel_list)
        print(rel)
        Request_url_id_list = f"https://www.yaofangwang.com/Medicine/getMedicineByIds?mids={rel}"
        yield scrapy.Request(
            url=Request_url_id_list,
            callback=self.get_yp_list,
            dont_filter=True
        )

    def get_yp_list(self, response):
        res = json.loads(response.text)["result"]
        item = YaofangwangItem()
        for data in res:
            "药品图地址，价格，药品名，规格，批准文号，生产厂家"
            item['img_path'] = "https:" + data.get("intro_image")
            item['price'] =data.get('price_min')
            item['name'] = data.get("medicine_name")
            item['gge'] = data.get("standard")
            item['pzwh'] = data.get("authorized_code")
            item['sccj'] = data.get("title")
            yield item
