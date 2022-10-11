# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/22 23:07
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : 凡科网.py
# @Software: PyCharm

"""
这么容易是因为凡科是闭包封装了一个js的自定义md5代码
如果发现加密代码在一个闭包里面的话，这个时候我们就可以直接去把整个闭包考过来
一般是都包含在里面的80%-90%
闭包是指==   （）（）；
"""


import execjs

node = execjs.get()
fanke = node.compile(open('./fanke.js',encoding='utf-8').read())

aa = 'md5("{}")'.format('asdfasdfasdf')

cc = fanke.eval(aa)
print(cc)

