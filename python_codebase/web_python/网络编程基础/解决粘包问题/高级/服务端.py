# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2514:34
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : 服务端.py
# @Software: PyCharm
__author__ = 'Small Fu'

import json
import struct
import socket, subprocess

ip_port = ('127.0.0.1', 8080)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(ip_port)  # 设置ip+prot
s.listen(5)  # 设置半链接池

while True:
    # 这个是判断有没有链接开通
    conn, addr = s.accept()
    print('客户端', addr)
    while True:
        # 设置传过来的命令大小 为1024bytes
        msg = conn.recv(1024)
        # 条件判断命令是否存在
        if not msg: break
        # 这里是执行系统命令
        res = subprocess.Popen(msg.decode('utf-8'), shell=True,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE)
        err = res.stderr.read()  # 读取输出内容
        if err:  # 看内容是否存在
            back_msg = err
        else:  # 不存在读取异常内容
            back_msg = res.stdout.read()

        headers = {
            'data_size': len(back_msg)
            
        }
        head_json = json.dumps(headers)
        head_json_bytes = bytes(head_json, encoding='utf-8')

        conn.send(struct.pack('i', len(head_json_bytes)))  # 先发报头的长度
        conn.send(head_json_bytes)  # 再发报头
        conn.sendall(back_msg)  # 在发真实的内容
    conn.close()
