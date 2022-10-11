# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/3119:33
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : 练习一SSHClient.py
__author__ = 'Small Fu'

import paramiko

# 创建ssh对象
ssh = paramiko.SSHClient()
# 设置允许连接不在线的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(
    hostname='192.168.110.141',
    port=22,
    username='root',
    password='123123'
)
# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls /')
# 获取命令结果
result = stdout.read()
print(result.decode('utf-8'))
# 关闭
ssh.close()
