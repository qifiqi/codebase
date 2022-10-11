# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2712:53
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : aa.py
# @Software: PyCharm_author__ = 'Small Fu'
from win32com import client as wc
import win32api
import win32con

for i in range(10):
    data = win32api.MessageBox(None, "Hello,pywin32!", "pywin32", win32con.MB_OK)
    print(data)
