# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import json


class SteamAutumnProjectPipeline:

    def __init__(self):
        # self.file_1 = open('./steam_discount.csv', 'a+', encoding='utf-8', newline='')
        # self.file_csv = csv.writer(self.file_1)
        # self.file_csv.writerow(
        #     ['游戏名字', '游戏标签', '价格', '优惠后的价格', '打折力度', '游戏地址', '游戏图片地址'])
        # self.file_json = open('./steam_discount.json', 'a+', encoding='utf-8')
        self.file_json = open('./steam_tab_content.json', 'a+', encoding='utf-8')


    def process_item(self, item, spider):
        # self.file_csv.writerow(
        #     [item['game_name'],
        #      item['game_label'],
        #      item['game_price'],
        #      item['game_after_discount_price'],
        #      item['game_discounts'],
        #      item['game_path'],
        #      item['game_img'],])
        json_str = json.dumps(dict(item), ensure_ascii=False)
        self.file_json.write(json_str+'\n')
        return item

    def claso_spider(self,spider):
        # self.file_1.close()
        self.file_json.close()
