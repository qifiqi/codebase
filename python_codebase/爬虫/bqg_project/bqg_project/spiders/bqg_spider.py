import scrapy
import time
from bqg_project.items import BookItem


class BqgSpiderSpider(scrapy.Spider):
    name = 'bqg_spider'
    allowed_domains = ['www.biquger.net']
    start_urls = ['http://www.biquger.net/']

    def parse(self, response):
        list_more_a = response.xpath(
            '//div[@class="main"]//div[@class="blockcontent"]/div[@class="more"]/a/@href').get()
        print(list_more_a)
        yield scrapy.Request(url=list_more_a, callback=self.parse_more)

    def parse_more(self, response):
        grid_table_list = response.xpath('//div[@id="content"]/table//tr')[1:]
        item = BookItem()
        for grid_table in grid_table_list:
            item['book_a'] = grid_table.xpath('./td[1]/a/@href').get()
            item['book_name'] = grid_table.xpath('./td[1]/a/text()').get()
            item['book_writer'] = grid_table.xpath('./td[3]/a/text()').get()
            item['book_datatime'] = grid_table.xpath('./td[4]/text()').get()
            item['book_statr'] = grid_table.xpath('./td[5]/text()').get()
            yield item
        try:
            next_a = 'http://www.biquger.net' + response.xpath('//div[@id="pagelink"]/a[@class="next"]/@href').get()
            print('*'*100)
            print(next_a)
            time.sleep(1)
            yield scrapy.Request(url=next_a, callback=self.parse_more)
        except Exception as ee:
            print(ee)
            print('结束')
