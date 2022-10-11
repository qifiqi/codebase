# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/24 12:57
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : wanmei.py
# @Software: PyCharm

import requests
import execjs
from lxml import etree

url = 'https://passport.wanmei.com/sso/login?service=passport&isiframe=1&location=2f736166652f'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
}
response = requests.get(url, headers=header).text
html = etree.HTML(response)
key = html.xpath('//input[@id="e"]/@value')[0]

aa = execjs.compile(open('./wanmei.js', 'r', encoding='utf-8').read()).call('pwd', '123123', key)
print(aa)
