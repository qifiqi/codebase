# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2412:53
# @Author  : 小符玩代码
# @Email   : 2737454073@qq.com
# @File    : 客户端.py
# @Software: PyCharm

import socket

# 1.创建客户端套接字
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.链接服务器
phone.connect(('127.0.0.1', 8080))
# 3.写/接收数据
phone.send('hello word! 啊啊啊'.encode('utf-8'))
print(phone.recv(1024).decode('utf-8'))
# 4.关闭
phone.close()
