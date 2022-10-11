# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/27 14:55
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : ydaoyun.py
# @Software: PyCharm

"""
salt: 16563128997256 是一个时间戳加一个随机的整数并转成str
sign: e42970a43c760675a40ac95407a56d63
    md5("fanyideskweb" + danci +salt+ "Ygy_4c=r#e#4EX^NUGUc5")
    md5加密吧一个字符串加上要翻译的单词，加上salt 加上一个字符串
lts: 1656312899725 时间戳
bv: 87675eb162e8c06260fd13bc61b5dcd4 吧useragent用md5加密
"""

import pprint
import execjs
import requests

file = open('./ydaoyun.js', 'r', encoding='utf-8').read()
node = execjs.compile(file)

i = input("请输入你要翻译的单词")
header = {
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
    'Cookie': 'UM_distinctid=18041679cf24e9-0a04af96a07d33-7b422e27-144000-18041679cf3104b; OUTFOX_SEARCH_USER_ID_NCOO=1479209558.4089954; OUTFOX_SEARCH_USER_ID="1349887205@10.105.137.204"; P_INFO=17670344644|1654445944|1|dict_logon|00&99|null&null&null#hun&431300#10#0|&0||17670344644; fanyi-ad-id=306808; fanyi-ad-closed=1; ___rl__test__cookies=1656314710166',
}
# 通过扣js获得了
# 'salt'
# 'sign'
# 'lts':
aa = node.call('aa', i)
# 这个是dv是加密的ueragent
bv = node.call('bv', header['User-Agent'])
data = {
    'i': i,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': aa['salt'],
    'sign': aa['sign'],
    'lts': aa['ts'],
    'bv': bv,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
session = requests.Session()
response = session.post(url=url, headers=header, data=data).json()
pprint.pprint(response)
