import scrapy, time
from scrapy.selector import Selector
from steam_autumn_project.items import SteamAutumnProjectItem


class SteamAutumnSpider1Spider(scrapy.Spider):
    name = 'steam_autumn_spider1'
    allowed_domains = ['steampowered.com']

    # start_urls = [
    #     f'https://store.steampowered.com/specials/https://store.steampowered.com/specials/#p={i}&tab=TopSellers' for i
    #     in range(0, 961, 0)]

    def start_requests(self):
        for i in range(0, 961, 1):
            # url = f'https://store.steampowered.com/specials/https://store.steampowered.com/specials/#p={i}&tab=TopSellers'
            url = f'https://store.steampowered.com/specials/#p={i}&tab=ConcurrentUsers'
            time.sleep(1)
            yield scrapy.Request(url=url, callback=self.parse_steam_steampowered, dont_filter=True)

    def parse_steam_steampowered(self, response):
        # sel = Selector(response)
        # sel.xpath().extract
        steampowered_list = response.xpath('//div[@id="TopSellersRows"]/a')
        for steampowered in steampowered_list:
            item = SteamAutumnProjectItem()
            item['game_name'] = steampowered.xpath('./div[@class="tab_item_content"]/div/text()').get()
            item['game_path'] = steampowered.xpath('./@href').get()
            item['game_img'] = steampowered.xpath('.//img/@src').get()
            game_label = steampowered.xpath('.//div[@class="tab_item_content"]//div['
                                            '@class="tab_item_top_tags"]/span/text()').extract()
            item['game_label'] = ''.join(game_label)
            item['game_discounts'] = steampowered.xpath(
                './div[@class="discount_block tab_item_discount"]/div/text()').get()
            item['game_price'] = steampowered.xpath(
                './div[@class="discount_block tab_item_discount"]/div[@class="discount_prices"]/div[1]/text()').get()
            item['game_after_discount_price'] = steampowered.xpath(
                './div[@class="discount_block tab_item_discount"]/div[@class="discount_prices"]/div[2]/text()').get()
            yield item
