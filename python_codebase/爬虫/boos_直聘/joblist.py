# -*- coding: utf-8 -*-
# All Rights Reserved
# @Time    : 2022/10/1812:07
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : joblist.py
__author__ = 'Small Fu'

import pprint
from urllib import parse
import requests

"""
url =- "https://www.zhipin.com/wapi/zpgeek/search/joblist.json"
https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=100010000&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page=2&pageSize=30

data = {
    "scene":" 1",
    "query":" 大数据",
    "city":" 100010000",
    "experience":" ",
    "degree":" ",
    "industry":" ",
    "scale":" ",
    "stage":" ",
    "position":" ",
    "salary":" ",
    "multiBusinessDistrict":" ",
    "page":" 1",
    "pageSize":" 30",
}

head = {
    'Accept': "application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",
    'referer': 'https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=100010000&page=2',
    "x-requested-with": "XMLHttpRequest"
}

注意在referer这里要注意，
注意重定向，



"""

data = {
    "scene": " 1",
    "query": " 大数据",  # 搜哦数据
    "city": " 100010000",  # 地区省
    "experience": "",  # 工作经验
    "degree": "",  # 学历
    "industry": "",
    "scale": "",
    "stage": "",
    "position": "",
    "salary": "",  # 薪资待遇
    "multiBusinessDistrict": "",  # 地级市
    "page": "1",  # 页码
    "pageSize": "30",  # 多少个
}

head = {
    'Accept': "application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",
    'referer': 'https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=100010000&page=2',
    "x-requested-with": "XMLHttpRequest",
    "cookie": "wd_guid=ead91b34-024d-40ec-86d4-509b556ef1c9; historyState=state; _bl_uid=e3lyF5mb9F7k95tehkCqf20kLUh4; __g=-; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE%26city%3D100010000%26page%3D2&r=&g=&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1666065818; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1666066019; __c=1666065817; __a=41867250.1657110525.1657120953.1666065817.40.5.8.40; __zp_stoken__=0a14eAGpYA2NzNyVwJix0HQxGMlA3AHlsaHYIByZdeRJbc3VxbHljGStnb3ZUKnIIJmQHbl99fhJsUH48UnZHXkIVKXFPQw10MTNfc3MpbWpUA3dMOncPBBxXLBBdazB3ZF01Zy13fBhybHo%3D",

}

url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json" + "?" + parse.urlencode(data).replace("+", "")


def joblist():
    try:
        response = requests.get(
            url=url,
            data=data,
            headers=head,
            params=5
        ).json()
        return response
    except Exception as f:
        print(f)


