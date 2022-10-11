# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2514:35
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : 客户端.py
# @Software: PyCharm
__author__ = 'Small Fu'

import json
import socket, time

# 创建连接
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置开发断开和ip
res = client.connect_ex(('127.0.0.1', 8080))

while True:
    # 发消息，加退出判断
    cmd = input('>>: ').strip()
    if len(cmd) == 0: continue
    if cmd == 'quit': break
    client.send(cmd.encode('utf-8'))
    # 接收长度
    head = client.recv(4) # 接收头的长度
    head_json_len = struct.unpack('i', head)[0]# 反解
    head_json = json.loads(client.recv(head_json_len).decode('utf-8'))# 获取出指定长度的报头
    data_len = head_json['data_size'] # 取出报头中的数据长度
    # 发送判断条件
    client.send('recv_ready'.encode('utf-8'))
    # 判断条件接收
    send_size = 0
    recv_size = 0
    data = b''
    while recv_size < data_len:
        data += client.recv(1024)
        recv_size += len(data)

    print(data.decode('utf-8'))
