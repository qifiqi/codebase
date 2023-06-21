import requests,time
from requests.structures import CaseInsensitiveDict
from requests.cookies import cookiejar_from_dict
class MoFish:
    def __init__(self,page=20):
        self.session = requests.session()
        self.session.headers = CaseInsensitiveDict({
            "authority": "api.tophub.fun",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "origin": "https://mo.fish",
            "pragma": "no-cache",
            "referer": "https://mo.fish/",
            "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82"
        })
        self.session.cookies =cookiejar_from_dict({
            "MoFish": "10c0d6ade558284d7be412d969983980"
        })
        self.page = page


    def page_GetAllInfoGzip(self,page=0,id_='1065'):
        url = "https://api.tophub.fun/v2/GetAllInfoGzip"
        params = {
            "id": id_,
            "page": page,
            "type": "pc"
        }


        response = self.session.get(url, params=params)
        data = response.json()


        for item in data['Data']['data']:
            print(item['Title'])
        print("page_GetAllInfoGzip page:" + str(data['Data']['page']))
        print("当前页"+str(page))
        time.sleep(10)
        if page == self.page:
            return
        else:
            page+=1
            self.page_GetAllInfoGzip(page)

if __name__ == '__main__':
    MoFish().page_GetAllInfoGzip()
