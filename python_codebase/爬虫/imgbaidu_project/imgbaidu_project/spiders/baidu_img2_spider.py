import scrapy
from imgbaidu_project.items import ImgbaiduProjectItem


class BaiduImg2SpiderSpider(scrapy.Spider):
    name = 'baidu_img2_spider'
    allowed_domains = ['baidu.com']
    start_urls = [
        'https://image.baidu.com/search/wiseindex']

    def parse(self, response):
        img_a = response.xpath('//div[@class="taotu"]/a')
        for img in img_a:
            item = ImgbaiduProjectItem()
            item['image_urls'] = img.xpath('./img/@src').extract()
            yield item
