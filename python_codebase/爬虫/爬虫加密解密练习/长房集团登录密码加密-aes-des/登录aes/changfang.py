# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/27 14:21
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : changfang.py
# @Software: PyCharm

import execjs

pwd = execjs.compile(open('./cahngfang.js','r',encoding='utf-8').read()).call('pwd','123123')
print(pwd)