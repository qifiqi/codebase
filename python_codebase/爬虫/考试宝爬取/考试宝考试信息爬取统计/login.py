# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/2610:02
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : login.py
__author__ = 'Small Fu'

from urllib.parse import quote,unquote

import requests

login_url = "https://www.zaixiankaoshi.com/api/user/login"

data = {"phone": "13635807017", "password": "sxg750819"}


# responses = requests.post(url=login_url,data=data)
# print(responses.json())


print(unquote("%22qvpRLDOko68d3MVEuHy044nKR/HjDD1pEQvFVlkJsx4=%22"))








