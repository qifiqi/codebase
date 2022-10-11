# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    book_path = scrapy.Field()
    book_img = scrapy.Field()
    author = scrapy.Field()
    comments = scrapy.Field()
    Recommended = scrapy.Field()
    Publishing = scrapy.Field()
    Published_date = scrapy.Field()
    price = scrapy.Field()
    Discount_price = scrapy.Field()
    Discount = scrapy.Field()
    Ebook_price = scrapy.Field()
