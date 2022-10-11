# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/3014:19
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : 代理.py
__author__ = 'Small Fu'

import requests

proxies = {
    "http": "http://58.20.184.187:9091",
    "https": "http://58.20.184.187:9091",
}
url = 'http://httpbin.org/ip'
response_json = requests.get(url=url, proxies=proxies).json()
print(response_json)
