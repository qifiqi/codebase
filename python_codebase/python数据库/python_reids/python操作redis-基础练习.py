# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/159:19
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : python操作redis-基础练习.py
__author__ = 'Small Fu'

import redis

red = redis.Redis(
    host="192.168.110.141",
    port=6379,
    password="123qweasd",
    decode_responses=True,  # 改成字符串简单来说就是设置中文显示
)
# 遍历keys
for key in red.keys():    # 遍历所有
# for key in red.keys("*8*"):  # 查看所有包含8的key
    print(key)  # 遍历所有key
    print(red.get(key))  # 获取key对应的values因为是二进制进行编码。decode（“utf-8”）

# for i in range(1000):
#     red.set(f"k{i}",f"这是第{i}个")
red.close()
