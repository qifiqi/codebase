# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2413:12
# @Author  : 小符玩代码
# @Email   : 2737454073@qq.com
# @File    : 服务端.py
# @Software: PyCharm

__author__ = 'Linhaifeng'

import socket

ip_port = ('127.0.0.1', 8081)
udp_server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 买手机
udp_server_sock.bind(ip_port)

while True:
    qq_msg, addr = udp_server_sock.recvfrom(1024)
    print('来自[%s:%s]的一条消息:\033[1;44m%s\033[0m' % (addr[0], addr[1], qq_msg.decode('utf-8')))
    back_msg = input('回复消息: ').strip()

    udp_server_sock.sendto(back_msg.encode('utf-8'), addr)
