import scrapy
from fbs100.items import Fbs100Item
from cryptography.hazmat.bindings.openssl.binding import Binding

class WwwBaiduComSpider(scrapy.Spider):
    name = 'gbs100'
    # allowed_domains = ['www.baidu.com']
    start_urls = ["https://www.maigoo.com/news/572609.html"]

    def parse(self, response):
        tr_list = response.css("tr.font14")
        item = Fbs100Item()
        for tr in tr_list:
            item["ids"], item['name'], item['price_yiyuan'], item['laiyuan'], item['age'], item['address'] = \
                tr.css(".md_td ::text").extract()
            yield item
