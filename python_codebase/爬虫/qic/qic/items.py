# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QicItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    img_path = scrapy.Field()
    price = scrapy.Field()
    dj = scrapy.Field()
    hot_index_1Bl1a = scrapy.Field()
    pass
