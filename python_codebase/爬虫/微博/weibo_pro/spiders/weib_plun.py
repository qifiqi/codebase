import feapder

class AirSpiderDemo(feapder.AirSpider):
    def start_requests(self):
        url = "https://weibo.com/ajax/statuses/buildComments"
        params = {
            "flow": "0",
            "is_reload": "1",
            "id": "4903446291155062",
            "is_show_bulletin": "2",
            "is_mix": "0",
            "count": "10",
            "uid": "1435723965",
            "fetch_level": "0"
        }
        yield feapder.Request(url, params=params, method="GET")

    def download_midware(self, request):
        request.headers = {
            "authority": "weibo.com",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "client-version": "v2.40.55",
            "pragma": "no-cache",
            "referer": "https://weibo.com/1435723965/N1rEx4Qu2",
            "sec-ch-ua": "^\\^Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "server-version": "v2023.05.23.1",
            "traceparent": "00-28c63e3b23344d1ffae5fb26c1463fc9-c52bb48d621b5c17-00",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50",
            "x-requested-with": "XMLHttpRequest",
            "x-xsrf-token": "QW6DGKjtwLShRL88VPN8yFOv"
        }
        request.cookies = {
            "SINAGLOBAL": "1176584170351.014.1683694614306",
            "ULV": "1683694614308:1:1:1:1176584170351.014.1683694614306:",
            "SUB": "_2A25JX1R-DeRhGeBL6FQT9CzIzz6IHXVqoHw2rDV8PUJbkNAGLUzVkW1NRwq7cSf6qCKAyIsVUQ1ULC7jGF_frBWl",
            "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WFygYPanwb1DNckiJ32h9U-5NHD95QcSKeceoBEShBEWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSo-0SozXeoBXentt",
            "WBPSESS": "hyTvPWv5o5Vgc0j0Bq7BmN_iSB4rI-FXeBX9akROR5mdtjldgGSCQXYqATJsVVszFrDEFdwcLx0nKjQgEKjvsRqi_2rIvIW8JUDA0bMCykrWdc7hBL2hc__fYIu4McHWgitJ9CmoBNhn0QqXh3QXVQ==",
            "XSRF-TOKEN": "QW6DGKjtwLShRL88VPN8yFOv"
        }
        return request

    def parse(self, request, response):
        print(response.json)
        print(response)


if __name__ == "__main__":
    AirSpiderDemo(thread_count=1).start()
