# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2522:00
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : client_one.py
# @Software: PyCharm
__author__ = 'Small Fu'

import socket

ip_prot = ('8.142.29.197', 8080)

client_one = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    text = input('输入:').strip()
    client_one.sendto(text.encode('utf-8'),ip_prot)
    res_text = client_one.recvfrom(1024)
    print(str(res_text[1])+'\n'+res_text[0].decode('utf-8'))
