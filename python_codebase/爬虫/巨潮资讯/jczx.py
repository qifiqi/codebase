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


def consumer_json(j, data: dict) -> None:
    """
    传入写入对象可以保存
    :param j: 文件对象
    :param data: 数据
    """
    records = data['records']
    for record in records:
        json_text = json.dumps(record, ensure_ascii=False)
        j.write(json_text + '\n')


def get_stock_list() -> json:
    """
    获取所有股票
    :return:
    """
    url_path = "http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1001"
    data = {
        'type': "2",
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
    data_json = req_session.post(url=url_path, data=data, headers=head).json()
    with open('./所有股票.json',"w",encoding="utf-8") as f:
        records = data_json['records']
        for record in records:
            json_text = json.dumps(record, ensure_ascii=False)
            f.write(json_text + '\n')
    return data_json





def get_date_search(scode: str, sdate: str, edate: str) -> json:
    """
    查询国内的每一个股票的详细
    :param scode:股票代码
    :param sdate:开始时间
    :param edate:结束时间
    :return:json数据
    """
    url_path = "http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1008"
    data = {
        "scode": scode,
        "sdate": sdate,
        "edate": edate,
        "ctype": "0"
    }
    head = {
        'Accept': "*/*",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'X-Requested-With': "XMLHttpRequest",
        'mcode': f"{getResCode()}",
        'Referer': 'https://webapi.cninfo.com.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
    }
    req_session = requests.session()
    return req_session.post(url=url_path, data=data, headers=head).json()


def coles(j):
    print('结束')
    f.close()
    j.close()
    sys.exit()


def main():
    j = open(f'./巨潮资讯-所有股票.json', 'a+', encoding='utf-8')
    times = input("请输入你要爬取数据的时间（2022-06-22）：")

    pprint.pprint(markets)
    for market in markets.keys():
        print(f'正在获取国内交易行情，\n地区:{markets[market]}\n时间{times}')
        data = requests_cninf_producer(market, times)
        consumer_json(j, data)
    coles(j)


if __name__ == '__main__':
    get_stock_list()
