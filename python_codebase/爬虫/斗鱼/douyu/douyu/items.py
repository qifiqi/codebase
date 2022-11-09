# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    type_name = scrapy.Field()
    username = scrapy.Field()
    title_ch = scrapy.Field()
    score = scrapy.Field()
    details_username = scrapy.Field()
    pass


class detailsDouyuItem(scrapy.Item):
    username = scrapy.Field()
    text = scrapy.Field()
    pass

