# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/22 9:47
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : 建筑市场监管局爬取.py
# @Software: PyCharm


"""
function(t, e, n) {
"use strict";
var a = n("d225")
  , r = n("b0b4")
  , i = (n("a481"),
n("6b54"),
n("bc3a"))
  , c = n.n(i)
  , o = n("c0d6")
  , s = n("4328")
  , l = n.n(s)
  , u = n("3452")
  , d = n.n(u)
  , p = n("5c96")
  , f = d.a.enc.Utf8.parse("jo8j9wGw%6HbxfFn") //这里编码成字节
  , m = d.a.enc.Utf8.parse("0123456789ABCDEF");
function h(t) { //传入解密数据
    var e = d.a.enc.Hex.parse(t)
      , n = d.a.enc.Base64.stringify(e)  // 使用beas64编码
      , a = d.a.AES.decrypt(n, f, {  // AES加密
        iv: m,
        mode: d.a.mode.CBC,  // CBC 方式
        padding: d.a.pad.Pkcs7
    })
      , r = a.toString(d.a.enc.Utf8);
    return r.toString()
}


"""
import json
import pprint

import requests
from Crypto.Cipher import AES

url = 'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15&total=450'
header = {
    'Referer': 'http://jzsc.mohurd.gov.cn/data/company',
    'timeout': '30000',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

data = requests.get(url, headers=header).text
key = b'jo8j9wGw%6HbxfFn'  # 要字节
iv = b'0123456789ABCDEF'

aes = AES.new(key, AES.MODE_CBC, iv)
data_asc = aes.decrypt(bytes.fromhex(data))
# res = str(data_asc, encoding='utf-8')

# length = len(res)
# un = ord(res[length - 1])
# res = res[0:length - un]
res = json.loads(data_asc)['data']['list']
pprint.pprint(res)