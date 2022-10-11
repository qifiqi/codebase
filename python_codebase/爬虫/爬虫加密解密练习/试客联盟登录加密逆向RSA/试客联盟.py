# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/25 14:10
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : 试客联盟.py
# @Software: PyCharm
import re

import requests
import execjs

urls = 'http://login.shikee.com/getkey?v=a190fe8a671fa1b84f16a115c3d80bd6'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'
}
data = requests.get(urls, headers).text
ras_n = re.findall('.*?"(.*?)"', data)[0]
node = execjs.compile(open('./sklm.js', 'r', encoding='utf-8').read())
jiamipassword = node.call('pwd', '123123', ras_n)
print(jiamipassword)

