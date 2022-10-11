import scrapy
import time
from imoot_project.items import ImootItem


class ImootSpiderSpider(scrapy.Spider):
    name = 'imoot_spider'
    allowed_domains = ['imoot.com']
    start_urls = ['https://www.imooc.com/']

    def parse(self, response):
        combat_a = 'https:' + response.xpath('//div[@id="nav"]/div/ul/li[3]/a/@href').get()
        # yield scrapy.Request(url=combat_a, callback=self.combat_parse, dont_filter=True)
        yield scrapy.Request(url=combat_a, callback=self.combat_parse_text, dont_filter=True)

    # def combat_parse(self, response):
    #     clearfix_list = response.xpath('//ul[@class="items clearfix"]/li')[1:]
    #     for clearfix in clearfix_list:
    #         combat_direction_a = 'https://coding.imooc.com' + clearfix.xpath('./a/@href').get()
    #         time.sleep(1)
    #         yield scrapy.Request(url=combat_direction_a, callback=self.combat_parse_classify, dont_filter=True)
    #
    # def combat_parse_classify(self, response):
    #     clearfix_list = response.xpath('//div[@class="two warp js-sort"]/ul[@class="items clearfix"]/li')[1:]
    #     for clearfix in clearfix_list:
    #         combat_classify_a = 'https://coding.imooc.com' + clearfix.xpath('./a/@href').get()
    #         time.sleep(2)
    #         yield scrapy.Request(url=combat_classify_a, callback=self.combat_parse_text, dont_filter=True)

    def combat_parse_text(self, response):
        classify_list = response.xpath('//ul[@class="course-list clearfix"]/li')
        for classify in classify_list:
            item = ImootItem()
            item['course_name'] = classify.xpath('./a/p[@class="title ellipsis2"]/text()').get()
            item['course_number'] = classify.xpath('./a/p[@class="one"]/span/text()').get()
            item['course_price'] = classify.xpath(
                './a/p[@class="two clearfix"]/span[@class="price l red bold"]/text()').get()
            yield item
        try:
            aaa = 'https://coding.imooc.com'+response.xpath('//div[@class="page"]/a[8]/@href').get()
            yield scrapy.Request(url=aaa, callback=self.combat_parse_text, dont_filter=True)
        except Exception as aa:
            print('ok')