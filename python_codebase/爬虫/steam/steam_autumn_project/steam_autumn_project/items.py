# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamAutumnProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_name = scrapy.Field()
    game_path = scrapy.Field()
    game_img = scrapy.Field()
    game_label = scrapy.Field()
    game_discounts = scrapy.Field()
    game_price = scrapy.Field()
    game_after_discount_price = scrapy.Field()

    pass
