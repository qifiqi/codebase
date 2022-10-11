# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YaofangwangItem(scrapy.Item):
    # define the fields for your item here like:
    img_path = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()
    gge = scrapy.Field()
    pzwh = scrapy.Field()
    sccj = scrapy.Field()
    pass
