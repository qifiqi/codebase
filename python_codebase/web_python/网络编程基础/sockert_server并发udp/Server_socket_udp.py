# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2521:48
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : Server_socket_udp.py
# @Software: PyCharm
__author__ = 'Small Fu'

import socketserver


# 继承类来写其中封装了链接创建，绑定ip
class MyRequestHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        client_data = self.request[0]
        client = self.request[1]
        client_address = self.client_address
        b''.decode('utf-8')
        print('客户端发来的数据:',client_data)
        client.sendto(client_data.upper(), client_address)


# 实现接口
server = socketserver.ThreadingUDPServer(('0.0.0.0', 8080), MyRequestHandler)
# 设置开始永远服务
server.serve_forever()
