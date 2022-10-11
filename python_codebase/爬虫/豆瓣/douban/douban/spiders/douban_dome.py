import scrapy
from douban.items import DoubanItem


class DoubanDomeSpider(scrapy.Spider):
    name = 'douban_dome'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    # start_urls = ['https://movie.douban.com/subject/1292052/']

    def parse(self, response):
        item = DoubanItem()
        douban_lists = response.xpath('//ol[@class="grid_view"]/li')
        for list in douban_lists:
            a = list.xpath('.//div[@class="pic"]/a/@href').extract_first()
            a2 = list.xpath('.//div[@class="pic"]/a/img/@alt').extract_first()
            print(a2)
            title = list.xpath('//div[@class="info"]/div[@class="hd"]/a/span[@class="title"]/text()').extract()
            item['title'] = title
            item['a'] = a
            yield scrapy.Request(url=a, callback=self.parse2, meta={'item': item})

    def parse2(self, response):
        item = response.meta['item']
        img = response.xpath('//div[@id="mainpic"]/a/img/@src').extract_first()
        director = response.xpath('//div[@director]//a/text()').extract_first()
        scriptwriter = response.xpath('//div[@class="subject clearfix"]/div[@id="info"]/span[2]/span['
                                      '@class="attrs"]/a/text()').extract()
        score = response.xpath('//div[@id="interest_sectl"]//strong/text()').extract_first()
        text = response.xpath('//div[@class="related-info"]//span[@class="short"]/span/text()').extract()
        item['img'] = img
        item['director'] = director
        item['scriptwriter'] = scriptwriter
        item['score'] = score
        item['text'] = text
        yield item
