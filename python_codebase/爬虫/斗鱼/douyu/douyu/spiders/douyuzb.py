import json
import pprint

import scrapy
from douyu.items import DouyuItem, detailsDouyuItem


class DouyuzbSpider(scrapy.Spider):
    name = 'douyuzb'

    # allowed_domains = ['douyu.com']
    # start_urls = ['https://www.douyu.com/directory']

    def start_requests(self):
        file = json.loads(open("斗鱼分类 .json", "r", encoding="utf-8").read())
        for fir in file.get("firstCategory"):
            for sec in fir.get("secondCategory"):
                url = f"https://www.douyu.com/gapi/rkc/directory/mixList/2_{sec.get('cate2Id')}/1"
                print(url)
                yield scrapy.Request(
                    url=url,
                    callback=self.parse,
                    meta={"url": f"https://www.douyu.com/gapi/rkc/directory/mixList/2_{sec.get('cate2Id')}/"}
                )
                # break

    def parse(self, response):
        url = response.meta["url"]
        res_json = json.loads(response.body)
        pgcnt = res_json.get("data").get("pgcnt")
        for rl in res_json.get("data").get("rl"):
            pprint.pp(rl)
            item = DouyuItem()
            item['type_name'] = rl.get("c2name")
            item['username'] = rl.get("nn")
            item['title_ch'] = rl.get("od")
            item['score'] = rl.get("ol")
            item['details_username'] = rl.get("url")

            yield scrapy.Request(
                url="https://www.douyu.com/betard" + rl.get("url"),
                callback=self.details,
                meta={"username": rl.get("nn")}
            )  # 这里是主播详情自己解析

            yield item
            # break
        for i in range(1, pgcnt + 1):
            yield scrapy.Request(
                url=f"{url}{i}",
                callback=self.parse_2
            )
            # break
        pass

    def parse_2(self, response):
        res_json = json.loads(response.body)
        pgcnt = res_json.get("data").get("pgcnt")
        for rl in res_json.get("data").get("cl"):
            item = DouyuItem()
            item['type_name'] = rl.get("c2name")
            item['username'] = rl.get("nn")
            item['title_ch'] = rl.get("od")
            item['score'] = rl.get("ol")
            item['details_username'] = rl.get("url")
            yield item

    def details(self, response):
        # 这里是主播详情自己解析
        item = detailsDouyuItem()
        item['username'] = response.meta["username"]
        item['text'] = json.dumps(json.loads(response.body),ensure_ascii=False)
        yield item
        pass
