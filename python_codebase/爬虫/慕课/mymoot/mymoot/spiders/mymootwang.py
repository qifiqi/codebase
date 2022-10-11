import scrapy
from mymoot.items import ImoocItem


class MymootwangSpider(scrapy.Spider):
    name = 'mymootwang'
    allowed_domains = ['www.imooc.com']
    start_urls = ['http://www.imooc.com']

    def parse(self, response):
        try:
            imooc_a = 'http://' + response.xpath(
                '//div[@id="header"]//ul[@class="nav-item l"]/li[3]/a/@href').extract_first()
            yield scrapy.Request(url=imooc_a, callback=self.parse_pages1, dont_filter=True)
        except Exception as err:
            print(err)
            print('全部结束')

    def parse_pages1(self, response):
        try:
            direction_list = response.xpath('//div[@class="type"]//ul[@class="items clearfix"]/li')[1:]
            for direction in direction_list:
                direction_a = 'http://www.imooc.com' + direction.xpath('./a/@href').extract_first()
                yield scrapy.Request(url=direction_a, callback=self.parse_pages2, dont_filter=True)
        except Exception as err:
            print(err)
            print('结束一个课')

    def parse_pages2(self, response):
        try:
            classify_list = response.xpath('//div[@class="type"]//div[@class="two warp js-sort"]/ul[@class="items clearfix"]/li')[1:]
            for classify in classify_list:
                classify_a = 'http://www.imooc.com' + classify.xpath('./a/@href').extract_first()
                print(classify_a)
                # yield scrapy.Request(url=classify_a, callback=self.parse_pages3)
        except:
            print('结束一个类别')


'''
    def parse_pages3(self, response):
        try:
            course_a = response.xpath('//div[@id="main"]/div[@class="course-list"]//a')[1:]
            for course in course_a:
                item = ImoocItem()
                cou_a = 'http://www.imooc.com' + course.xpath('./@href').extract_first()
                cou_title = course.xpath('.//P[@class="title ellipsis2"]/text()').extract_first()
                cou_num = course.xpath('.//P[@class="one"]/text()').extract_first()
                item['course_title'] = cou_title
                item['course_a'] = cou_a
                item['course_num'] = cou_num
                yield item
            course_page = response.xpath('//div[@id="main"]/div[@class="page"]/a')[-2]
            yield scrapy.Request(url=course_page, callback=self.parse_pages3)
        except Exception as err:
            print(err)
            print('结束一个')
'''
