# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json, csv


class DangdangPipeline:
    def __init__(self):
        self.file_csv = open('dangdang.csv', 'a+', encoding='utf-8', newline='')
        self.dang_csv = csv.writer(self.file_csv)
        self.dang_csv.writerow(
            ['图书名字',
             '图书作者',
             '图书出版社',
             '图书评价数',
             '图书推荐指数',
             '图书原价',
             '图书折后价',
             '图书折扣',
             '图书电子书价格',
             '图书出版时间',
             '图书地址',
             '图书图片地址'
             ])
        self.file_json = open('dangdang.json', 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        self.dang_csv.writerow([
            item['name'],
            item['author'],
            item['Publishing'],
            item['comments'],
            item['Recommended'],
            item['price'],
            item['Discount_price'],
            item['Discount'],
            item['Ebook_price'],
            item['Published_date'],
            item['book_path'],
            item['book_img'],
        ])
        dangdang_json = json.dumps(dict(item), ensure_ascii=False)
        self.file_json.write(dangdang_json + '\n')
        return item

    def close_spider(self, spider):
        self.file_csv.close()
        self.file_json.close()
