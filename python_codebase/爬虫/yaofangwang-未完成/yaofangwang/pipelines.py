# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import os

import requests
from itemadapter import ItemAdapter
from yaofangwang.settings import IMG_PATH, DEFAULT_REQUEST_HEADERS


class YaofangwangPipeline:
    def process_item(self, item, spider):
        with open("./中西药.csv", "a+", encoding="utf-8-sig", newline="") as ff:
            csv_file = csv.writer(ff)
            csv_file.writerow(list(dict(item).values()))

        # IMG_PATH = "./imgs"
        if not os.path.exists(IMG_PATH):
            os.mkdir(IMG_PATH)

        with open(f"{IMG_PATH}/{item['name']}.gif", "wb+") as img:
            res = requests.get(item["img_path"], headers=DEFAULT_REQUEST_HEADERS).content
            print(item['name'])
            img.write(res)
            img.close()

        return item
