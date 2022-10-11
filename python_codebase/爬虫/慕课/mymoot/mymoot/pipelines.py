# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class MymootPipeline:

    def __init__(self):
        self.course = open('imooc.json', 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        jsonstr = json.dumps(dict(item), ensure_ascii=False)
        self.course.write(jsonstr + '\n')
        return item

    def close_spider(self):
        self.course.close()
