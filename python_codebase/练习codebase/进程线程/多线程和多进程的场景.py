# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2922:16
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : 多线程和多进程的场景.py
__author__ = 'Small Fu'

import os
import time
from multiprocessing import Process
from threading import Thread

# 计算密集型
"""
def ww():
    a = 0
    for i in range(100000000):
        a *= i


if __name__ == '__main__':
    li = []
    start_time = time.time()
    print(os.cpu_count())
    for i in range(8):
        # p = Process(target=ww)# 11.505161046981812
        # p.start()
        # li.append(p)
        p = Thread(target=ww)   # 31.098137140274048
        p.start()
        li.append(p)

    for i in li:
        i.join()

    print(time.time() - start_time)

"""


def ww():
    time.sleep(2)


if __name__ == '__main__':
    li = []
    start_time = time.time()
    print(os.cpu_count())
    for i in range(200):
        # p = Process(target=ww)#20.760708332061768
        # p.start()
        # li.append(p)
        p = Thread(target=ww)#2.0361764430999756
        p.start()
        li.append(p)

    for i in li:
        i.join()

    print(time.time() - start_time)
