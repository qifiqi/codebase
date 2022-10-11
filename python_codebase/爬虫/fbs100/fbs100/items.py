# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Fbs100Item(scrapy.Item):
    # define the fields for your item here like:
    ids = scrapy.Field()
    name = scrapy.Field()
    price_yiyuan = scrapy.Field()
    laiyuan = scrapy.Field()
    age = scrapy.Field()
    address = scrapy.Field()
    pass
