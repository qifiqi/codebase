# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2413:12
# @Author  : 小符玩代码
# @Email   : 2737454073@qq.com
# @File    : 服务端.py
# @Software: PyCharm


import socket

# AF_INET = 基于互联网,SOCK_STREAM= 流式协议 =》tcp协议
# SOCK_DGRAM = 报文协议=》udp协议
# 1创建套接字对象
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.绑定ip地址
phone.bind(('127.0.0.1', 8080))
# 3.开始监听listen
phone.listen(5)  # 数字是半连接池的大小
# 4等待请求接受（） - >（套接字对象，地址信息）
# 等待传入连接。返回一个表示连接的新套接字，以及客户端的地址。对于 IP 套接字，地址信息是一对 (hostaddr, port)。
conn, client_addr = phone.accept()
# print(conn)
# print(client_addr)
# 5 接收 这里指定数据大小是1024bytes类型，收到的样式bytes类型
data = conn.recv(1024)
print(data.decode('utf-8'))
# 发数据
conn.send(data.upper())

# 6. 断开链接
conn.close()  # 关闭链接
# 7。关闭套接字=关闭了服务器
# phone.close()

