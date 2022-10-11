# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv


class ImgbaiduProjectPipeline:
    def __init__(self):
        # self.conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='')
        self.file = open('./img_src.csv', 'a+', encoding='utf-8')
        self.csv_aa = csv.writer(self.file, delimiter=',')
        self.csv_aa.writerow(['图片地址'])

    def process_item(self, item, spider):
        self.csv_aa.writerow([item['img_src']])
        return item

    def close_spider(self, spider):
        self.file.close()
