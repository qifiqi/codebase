# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json, csv, os
from itemadapter import ItemAdapter

from douyu.items import DouyuItem, detailsDouyuItem
from douyu.settings import DETAILS_PATH


class DouyuPipeline:
    def __init__(self):

        self.file_json = open('斗鱼主播.json', "a+", encoding="utf-8")
        self.file = open('斗鱼主播.csv', "a+", encoding="utf-8", newline="")
        self.file_csv = csv.writer(self.file)
        self.file_csv.writerow(["游戏类型", "主播", "称号", "热度", "主播详情链接"])

        if not os.path.exists(DETAILS_PATH):
            os.mkdir(DETAILS_PATH)

    def process_item(self, item, spider):
        if isinstance(item, DouyuItem):
            self.file_json.write(json.dumps(dict(item), ensure_ascii=False) + ',\n')
            self.file_csv.writerow(list(dict(item).values()))
            return item
        elif isinstance(item, detailsDouyuItem):
            with open(f"{DETAILS_PATH}{item['username']}.json", "w+", encoding="utf-8") as f:
                f.write(item["text"])
            return item
        return item


def close_spider(self, spider):
    self.file_json.close()
    self.file.close()
