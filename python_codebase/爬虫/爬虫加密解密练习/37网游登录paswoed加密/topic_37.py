# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2710:24
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : topic_37.py
# @Software: PyCharm
__author__ = 'Small Fu'

import time

import execjs
import requests
node = execjs.get()
js = node.compile(open('./js_pasword_37.js', 'r', encoding='utf-8').read())
data = 'td("{}")'.format('123qweasdzxc')
password = js.eval(data)
username = '123qweasd_1111'
times = int(time.time()*1000)
url = f'https://my.37.com/api/login.php?callback=jQuery18308754949592451187_1658889409799&action=login&login_account={username}&password={password}&ajax=0&remember_me=1&save_state=1&ltype=1&tj_from=103&s=1&tj_way=1&_={times}'

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
    'referer':'https://my.37.com/login.html',
}

response = requests.get(url,head).text

