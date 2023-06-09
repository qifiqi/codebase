# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/6/313:37
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : newrank.cn榜单案例.py
__author__ = 'Small Fu'
import requests

def Ntoken():
    pass

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Origin": "https://www.newrank.cn",
    "Referer": "https://www.newrank.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "content-type": "application/x-www-form-urlencoded",
    "n-token": "3b2f8f99af0545cc989cfae76477d9bf",
    "sec-ch-ua": "^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^"
}

url = "https://gw.newrank.cn/api/main/xdnphb/main/v1/day/rank"
data = {
    "end": "2023-06-02",
    "start": "2023-06-02",
    "rank_name": "文化",
    "rank_name_group": "生活"
}
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)