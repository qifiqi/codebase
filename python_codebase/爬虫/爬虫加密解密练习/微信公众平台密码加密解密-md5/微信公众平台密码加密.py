# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/21 20:13
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : 微信公众平台密码加密.py
# @Software: PyCharm
import execjs

node = execjs.get()

aa = node.compile(open('./wx.js', encoding='utf-8').read())

cc = aa.eval('pwd("{}")'.format('2002asdfasdf'))
print(cc)
