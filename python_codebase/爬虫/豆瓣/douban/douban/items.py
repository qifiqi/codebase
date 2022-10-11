# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    a = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    director = scrapy.Field()
    scriptwriter = scrapy.Field()
    score = scrapy.Field()
    text = scrapy.Field()
