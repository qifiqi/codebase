# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import json

from itemadapter import ItemAdapter


class Fbs100Pipeline:
    def process_item(self, item, spider):
        with open("./fbs100.json","a+",encoding="utf-8") as f:
            f.write(json.dumps(dict(item),ensure_ascii=False)+",\n")
            f.flush()

        with open("./福布斯.csv","a+",encoding="utf-8") as file:
            file_csv = csv.writer(file)
            file_csv.writerow(list(dict(item).values()))
        return item


