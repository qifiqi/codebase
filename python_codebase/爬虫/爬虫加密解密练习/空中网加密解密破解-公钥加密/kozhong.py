# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/26 13:40
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : kozhong.py
# @Software: PyCharm
import json
import re
import requests
import execjs

urls = 'https://sso.kongzhong.com/ajaxLogin?j=j&jsonp=j&service=https://passport.kongzhong.com/&_=1656221917552'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
    'Referer': 'https://passport.kongzhong.com/',
}
response = requests.get(url=urls, headers=header).text
zz = '.*?\((.*?)\)'
dc = re.findall(zz, response)[0]
dc = json.loads(dc)['dc']

password_jiami = execjs.compile(open('./kozhong.js', 'r', encoding='utf-8').read()).call('pwd', '123123', dc)
print(password_jiami)
