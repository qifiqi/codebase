# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class DoubanPipeline:
    # 或者用
    # def open_spider(self):
    # 这个方法也可以和init一样都是用于一次打卡文件
    def __init__(self):
        self.file = open('douban.csv', 'w', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file, delimiter=';')
        self.writer.writerow(['电影名字', '电影地址', '电影图片', '导演', '编剧', '评分', '简单介绍'])

    def process_item(self, item, spider):
        self.writer.writerow((item['title'], item['a'], item['img'], item['director'], item['scriptwriter'], item['score'], item['text'] ))
        return item

    def close_spider(self, spider):
        self.file.close()
