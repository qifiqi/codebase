# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/23 16:08
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : jczx.py
# @Software: PyCharm
import json
import pprint
import sys
import time

import requests
import execjs

with open('./mcode.js', 'r', encoding='utf-8') as f:
    js = f.read()
getResCode = execjs.compile(js).call('getResCode')


markets = {
    'CFFE': '中国金融期货交易所',
    'DCE': '大连商品交易所',
    'SHFE': '上海期货交易所',
    'ZCE': '郑州商品交易所',
    'HKG': '香港联合交易所',
    'SHE': '上海证券交易所',
    'SZE': '深圳证券交易所',
}


def requests_cninf_producer(market, times):
    url_path = 'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'
    data = {
        'tdate': times,
        'market': market,
    }
    head = {
        'Accept': "*/*",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'X-Requested-With': "XMLHttpRequest",
        'mcode': f"{getResCode}",
        'Referer': 'https://webapi.cninfo.com.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
    }
    req_session = requests.session()
    return req_session.post(url=url_path, data=data, headers=head).json()


def consumer_json(j,data):
    records = data['records']
    for record in records:
        json_text = json.dumps(record, ensure_ascii=False)
        j.write(json_text + '\n')


def coles(j):
    print('结束')
    f.close()
    j.close()
    sys.exit()


def main():
    global market
    times = input("请输入你要爬取数据的时间（2022-06-22）：")
    pprint.pprint(markets)
    market = input('数据你要的地区')
    if times == "":
        times = time.strftime('%Y-%m-%d')
    if market == "":
        market = 'SZE'
    print(f'正在获取国内交易行情，\n地区:{markets[market]}\n时间{times}')
    data = requests_cninf_producer(market, times)
    j = open(f'./巨潮资讯-{market}.json', 'w', encoding='utf-8')
    consumer_json(j,data)
    coles(j)


if __name__ == '__main__':
    main()
