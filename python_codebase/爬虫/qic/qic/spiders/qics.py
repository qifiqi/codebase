import scrapy
from qic.items import QicItem


class QicsSpider(scrapy.Spider):
    name = 'qics'
    # allowed_domains = ['qic.com']
    start_urls = ['https://top.baidu.com/board?tab=car']



    def parse(self, response):
        item = QicItem()
        div_css = response.css("div.category-wrap_iQLoo")
        for div in div_css:
            item["img_path"] = div.css(".img-wrapper_29V76 img::attr(src)").extract_first()
            item["name"] = div.css(".c-single-text-ellipsis::text").extract_first().strip()
            item["price"], item["dj"] = div.css(".intro_1l0wp ::text").extract()
            item["hot_index_1Bl1a"] = div.css(".hot-index_1Bl1a::text").extract_first()
            print(item)
            yield item
