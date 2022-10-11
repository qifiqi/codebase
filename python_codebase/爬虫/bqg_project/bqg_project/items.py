# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BqgProjectItem(scrapy.Item):
    # define the fields for your item here like:
    pass


class BookItem(scrapy.Item):
    book_a = scrapy.Field()
    book_name = scrapy.Field()
    book_writer = scrapy.Field()
    book_datatime = scrapy.Field()
    book_statr = scrapy.Field()

    pass
