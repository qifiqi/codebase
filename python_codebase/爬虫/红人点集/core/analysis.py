# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/721:14
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : analysis.py
__author__ = 'Small Fu'
"""
这个模块用于，数据处理
"""
import json
from pprint import pprint

json_files = json.loads(open('../static/json_file_dir/ks0316.json','r',encoding='utf-8').read())

for user in json_files.get("data").get("rankList"):
    pprint(user)

