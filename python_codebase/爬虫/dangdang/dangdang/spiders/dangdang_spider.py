import scrapy
from scrapy import Request
from dangdang.items import DangdangItem
import time
from tqdm import tqdm


class DangdangSpiderSpider(scrapy.Spider):
    name = 'dangdang_spider'
    allowed_domains = ['dangdang.com']

    # start_urls = ['http://bang.dangdang.com/']
    def start_requests(self):
        for i in range(1, 26):
            time.sleep(5)
            url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-' + str(i)
            print(url)
            yield Request(url=url, callback=self.book_now_parse, dont_filter=False)

    # def parse(self, response):
    #     book_blank = response.xpath('//div[@id="hd"]/div[@class="sub"]/ul/li[1]/a/@href').get()
    #     print(book_blank)
    #     yield Request(url=book_blank, callback=self.book_blank_parse)
    #
    # def book_blank_parse(self, response):
    #     book_like_now = response.xpath('//div[2]/div[1]/p[1]/span[2]/a[2]/@href').get()
    #     print(book_like_now)
    #     yield Request(url=book_like_now, callback=self.book_now_parse, dont_filter=False)

    def book_now_parse(self, response):
        book_now_list = response.xpath('//div[@class="bang_list_box"]/ul/li')
        for book_now in book_now_list:
            item = DangdangItem()
            item['name'] = book_now.xpath('./div[@class="name"]/a/text()').get()
            item['book_path'] = book_now.xpath('./div[@class="name"]/a/@href').get()
            item['book_img'] = book_now.xpath('./div[@class="pic"]/a/img/@src').get()
            item['author'] = book_now.xpath('./div[@class="publisher_info"]/a/@title').get()
            item['comments'] = book_now.xpath('./div[@class="star"]/a/text()').get()
            item['Recommended'] = book_now.xpath('./div[@class="star"]/a/span[@class="tuijian"]/text()').get()
            item['Publishing'] = book_now.xpath('./div[@class="publisher_info"]/a/text()').get()
            item['Published_date'] = book_now.xpath('./div[@class="publisher_info"]/span/text()').get()
            item['price'] = book_now.xpath('./div[@class="price"]/p[1]/span[@class="price_n"]/text()').get()
            item['Discount_price'] = book_now.xpath('./div[@class="price"]/p[1]/span[@class="price_r"]/text()').get()
            item['Discount'] = book_now.xpath('./div[@class="price"]/p[1]/span[@class="price_s"]/text()').get()
            item['Ebook_price'] = book_now.xpath('./div[@class="price"]/p[2]/span/text()').get()
            yield item
