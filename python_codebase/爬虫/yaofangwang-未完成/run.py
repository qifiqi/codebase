import requests
from scrapy import cmdline
from yaofangwang.settings import DEFAULT_REQUEST_HEADERS

cmdline.execute("scrapy crawl yaofangwangs".split())


# with open("./97f18f5f12664a16bec409a4cb186099.ttf","wb+") as f:
#     res = requests.get("https://www.yaofangwang.com/fonts/97f18f5f12664a16bec409a4cb186099.ttf",DEFAULT_REQUEST_HEADERS)
#     f.write(res.content)
#     f.close()


font = {
    "&#x351D;": 0,
    "&#x3E73;": 1,
    "&#xB561;": 2,
    "&#x0F88;": 3,
    "&#xCC5E;": 4,
    "&#x1ECC;": 5,
    "&#xE171;": 6,
    "&#x0FFF;": 7,
    "&#x2FCF;": 8,
    "&#x2992;": 9,
}

