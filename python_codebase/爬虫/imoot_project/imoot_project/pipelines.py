# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class ImootProjectPipeline:
    def __init__(self):
        self.file = open('../imoot.json', 'a+')

    def process_item(self, item, spider):
        jjj = json.dumps(dict(item),ensure_ascii=False)
        self.file.write(jjj + '\n')
        return item

    def close_spider(self, spider):
        self.file.close()
