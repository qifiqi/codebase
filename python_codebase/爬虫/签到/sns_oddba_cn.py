import requests
import datetime
import time
import random
from requests.structures import CaseInsensitiveDict


class snsClass:
    def __init__(self):
        self.headers = {
            "authority": "sns.oddba.cn",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://sns.oddba.cn",
            "pragma": "no-cache",
            "referer": "https://sns.oddba.cn/sign",
            "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67",
            "x-requested-with": "XMLHttpRequest",
        }
        self.session = requests.session()
        self.session.headers = CaseInsensitiveDict(self.headers)

    def login(self):
        url = "https://sns.oddba.cn/wp-content/themes/LightSNS/module/action/login.php"
        data = {
            "username": "小符demo",
            "password": "2002308FUqing",
            "ticket": "",
            "randstr": "",
        }

        responses = self.session.post(url, data=data)
        print(responses.text)
        print(responses.cookies)
        print("-----登录\n")
        time.sleep(random.randint(1, 3))

    def signInOnThatDay(self):
        day = datetime.date.today().day
        print("签到:" + str(day))
        url = "https://sns.oddba.cn/wp-content/themes/LightSNS/module/action/sign.php"
        data = {
            "sign": "1",
            "ticket": "",
            "randstr": ""
        }
        responses = self.session.post(
            url=url,
            data=data,
        )
        print(responses.text)
        time.sleep(random.randint(1, 3))

    def outlog(self):
        self.session.post(
            "https://sns.oddba.cn/wp-content/themes/LightSNS/module/update/profile.php",
            data={"login_out": 1},
        )
        print("-----登出\n")
        time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    sns = snsClass()
    sns.outlog()
    sns.login()
    sns.signInOnThatDay()
    sns.outlog()
