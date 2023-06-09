import csv

import feapder


class AirSpiderDemo(feapder.AirSpider):
    def __init__(self, thread_count=None):
        super().__init__(thread_count)
        self.file_csv = None
        self._files = None

    def start_requests(self):
        for i in range(1, 35):
            url = "https://shopee.ph/api/v4/recommend/recommend"
            params = {
                "bundle": "shop_page_product_tab_main",
                "limit": "30",
                "offset": str(i * 30),
                "section": "shop_page_product_tab_main_sec",
                "shopid": "160357616"
            }
            yield feapder.Request(url, params=params, method="GET")

    def start_callback(self):
        self._files = open("./demo3.csv", "a+", encoding="utf-8", newline="")
        self.file_csv = csv.writer(self._files)
        self.file_csv.writerow(['商品Id', '商品名字', '价格', '月销量(隐藏字段）', '总销量'])

    def end_callback(self):
        self._files.close()

    def download_midware(self, request):
        request.headers = {
            "authority": "shopee.ph",
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "if-none-match-": "55b03-25879a9028c8bbab7c6e7e7a6eda128c",
            "referer": "https://shopee.ph/shop/160357616/search?page=1&sortBy=pop",
            "sec-ch-ua": "^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "x-api-source": "pc",
            "x-requested-with": "XMLHttpRequest",
            "x-shopee-language": "en"
        }
        request.cookies = {
            "_gcl_au": "1.1.1977370942.1685099422",
            "SPC_SI": "02VsZAAAAABPMTBPa1FNc/KrZAAAAAAAcnY3aTVmU2g=",
            "_QPWSDCXHZQA": "55ebd7ec-a94e-4d7d-fe00-020356dfd1a9",
            "SPC_T_ID": "+O6EhBNGNpNguiaYKDptFdOn8LnCZib1t9rWSm5/haydhAldbaY1vqh5O8Motkn0CBQC740DRFH09BkbI0WgVnBeU3KnnmfjnO1jDw2G3TFL/nikLTW1roAZDBzX43bnCvsxAAiXOm6CJ0i/cFE9vZmHtCQan5iTxF7ZTyvv65U=",
            "SPC_T_IV": "eUhOd21sVkxiR2JUeFZIeA==",
            "SPC_F": "3Zer5zItoMtch4HBcAumLV0ukT4e4Sb7",
            "REC_T_ID": "ebf4616c-fbb5-11ed-8878-2cea7fb0a9e4",
            "SPC_R_T_ID": "+O6EhBNGNpNguiaYKDptFdOn8LnCZib1t9rWSm5/haydhAldbaY1vqh5O8Motkn0CBQC740DRFH09BkbI0WgVnBeU3KnnmfjnO1jDw2G3TFL/nikLTW1roAZDBzX43bnCvsxAAiXOm6CJ0i/cFE9vZmHtCQan5iTxF7ZTyvv65U=",
            "SPC_R_T_IV": "eUhOd21sVkxiR2JUeFZIeA==",
            "_gid": "GA1.2.1309913745.1685099442",
            "__LOCALE__null": "PH",
            "csrftoken": "gznHShiK2tNMzismqIlCYwiQ88uZv77r",
            "_fbp": "fb.1.1685114826132.1566149267",
            "AMP_TOKEN": "^%^24NOT_FOUND",
            "_ga": "GA1.1.1245348286.1685099431",
            "shopee_webUnique_ccd": "ph4kMUCLndQUPWaWDrDn^%^2FQ^%^3D^%^3D^%^7Cul9FiRCxK3BDzXFSazDKjhCYf8QyTk2cGnY2dDBY5g56PHYk0L0t9ThyDIbgRZG1jFBNGDV1Nf4aNBxI9OEpdpu6XK6R^%^2FAHHe9c^%^3D^%^7Cc^%^2FD^%^2Fs99lRS5qfygO^%^7C06^%^7C3",
            "ds": "a338f0f54538168bee8d0557ef5494d8",
            "_ga_CB0044GVTM": "GS1.1.1685113548.2.1.1685115428.60.0.0"
        }
        return request

    def parse(self, request, response):
        for i in response.json["data"]["sections"][0]["data"]["item"]:
            self.file_csv.writerow([
                i["itemid"], i["name"], i["price"] / 1000, i["sold"], i["historical_sold"]
            ])


if __name__ == "__main__":
    AirSpiderDemo(thread_count=12).start()
