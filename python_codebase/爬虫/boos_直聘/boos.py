# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/6 21:38
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : boos.py
# @Software: PyCharm
import pprint
from hyper.contrib import HTTP20Adapter
import requests

url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=100010000&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page=2&pageSize=30'

head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",
    'referer': 'https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=100010000&page=2',
    ':authority': 'www.zhipin.com',
    ':method': 'GET',
    ':scheme': 'https',
    'Accept': "application/json, text/plain, */*",
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    ':path': '/wapi/zpgeek/search/joblist.json?scene=1&query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=100010000&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page=2&pageSize=30',
    'cookie': 'wd_guid=ead91b34-024d-40ec-86d4-509b556ef1c9; historyState=state; _bl_uid=e3lyF5mb9F7k95tehkCqf20kLUh4; __fid=6d42c602eb95375c7683a379973f7855; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1657111291,1657115569; acw_tc=0a099dd616571209529218647e016d78518baf57542f9a6487b1ead976c2e4; __g=-; __zp_stoken__=3985dKT4MQl06UCpaZmYVRjQjBS1fbGpSPDpGeAtyNgRfGxVLXUJMHyZqO0xENHhHfRwSMF5HezUxMGYEEWR1Dll%2BKxYEWjl0cTwNSzJ%2BFB8Je1YDdzYHOgNIQA03CVwMPyUgTkRndjx4dDQ%3D; __c=1657120953; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE%26city%3D100010000%26page%3D1&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __a=41867250.1657110525.1657114750.1657120953.22.4.2.22',
}

session = requests.session()
session.mount(url, HTTP20Adapter())

response = session.get(url, headers=head).json()
print(response)
for i in response['zpData']['jobList']:
    lid = i['lid']
    securityId = i['securityId']
    url2 = f'https://www.zhipin.com/job_detail/2137e4ae5468ed590XVz39W8GFM~.html?lid={lid}&securityId={securityId}'
    session.mount(url2, HTTP20Adapter())
    response2 = session.get(url2, headers=head)
    print(response2.text)
    break
