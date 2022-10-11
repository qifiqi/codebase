# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImootProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ImootItem(scrapy.Item):
    # define the fields for your item here like:
    course_name = scrapy.Field()
    course_number = scrapy.Field()
    course_price = scrapy.Field()
