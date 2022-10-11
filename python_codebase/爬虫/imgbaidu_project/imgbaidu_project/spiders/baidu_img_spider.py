import scrapy
from imgbaidu_project.items import ImgbaiduProjectItem


class BaiduImgSpiderSpider(scrapy.Spider):
    name = 'baidu_img_spider'
    allowed_domains = ['baidu.com']
    start_urls = ['https://image.baidu.com/search/wiseindex']
    i = 0

    def parse(self, response):
        classify_a_list = response.xpath('//div[@class="img_list"]/a')
        for classify in classify_a_list:
            classify_a = 'https://image.baidu.com' + classify.xpath('./@href').get()
            classify_title = classify.xpath('./text()').get()
            title = {"title": classify_title}
            yield scrapy.Request(url=classify_a, callback=self.parse_classify, dont_filter=True,meta=title)
            print(classify_a+'8'*88)

    def parse_classify(self, response):
        classify_a = response.xpath('//div[@class="mb ct b"]/a')
        for classify in classify_a:
            item = ImgbaiduProjectItem()
            item['img_src'] = classify.xpath('./img/@src').get()
            yield item
        next_a = 'https://image.baidu.com' + response.xpath('/html/body/div[4]/a/@href').get()
        print(f'当前是第{BaiduImgSpiderSpider.i+1}页')
        yield scrapy.Request(url=next_a, callback=self.parse_classify,dont_filter=True)
