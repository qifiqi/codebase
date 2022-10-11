# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2912:34
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : read_comics.py
# @Software: PyCharm
__author__ = 'Small Fu'

import requests
from lxml import etree

head = {
    # 'if-none-match': "5a866-KZkFyNl48jAdvvUx6H+W6QXxoQ4",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
}
url = 'https://www.kuaikanmanhua.com/web/comic/151843/'
response = requests.get(url, head)
print(response.encoding)
print(response.text)
