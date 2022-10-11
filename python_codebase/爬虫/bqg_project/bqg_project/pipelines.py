# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class BqgProjectPipeline:
    def __init__(self):
        self.bbb = open('./bqg.csv', 'a+', encoding='utf-8', newline='')
        self.csv_bqg = csv.writer(self.bbb, delimiter=',')
        self.csv_bqg.writerow(['文章名称', '作者', '更新时间', '状态', '文章地址'])

    def process_item(self, item, spider):
        self.csv_bqg.writerow([item['book_name'],
                               item['book_writer'],
                               item['book_datatime'],
                               item['book_statr'],
                               item['book_a']])
        return item

    def close_spider(self):
        self.bbb.close()
