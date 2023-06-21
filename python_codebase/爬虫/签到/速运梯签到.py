# -*- coding: utf-8 -*-

import time

import requests
from requests.structures import CaseInsensitiveDict


class sutoyunClass:
    def __init__(self):
        self.headers = {
            "authority": "suyunti1.com",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://suyunti1.com",
            "pragma": "no-cache",
            "referer": "https://suyunti1.com/auth/login",
            "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51",
            "x-requested-with": "XMLHttpRequest"
        }
        self.session = requests.session()
        self.session.headers = CaseInsensitiveDict(self.headers)

    @staticmethod
    def _requests_to_string(response):
        print(response.json())

    def login(self):
        url = "https://suyunti1.com/auth/login"
        data = {
            "email": "2737454073@qq.com",
            "passwd": "123qweasdzxc,./?",
            "code": ""
        }
        response = self.session.post(url, data=data)
        self._requests_to_string(response)

    def signIn(self):
        url = 'https://suyunti1.com/user/checkin'
        response = self.session.post(url)
        self._requests_to_string(response)

    def outlogin(self):
        url = 'https://suyunti1.com/user/logout'
        response = self.session.post(url)
        print('登出')


if __name__ == '__main__':
    expressElevator = sutoyunClass()
    expressElevator.login()
    time.sleep(3)

    expressElevator.signIn()
    time.sleep(3)

    expressElevator.outlogin()
