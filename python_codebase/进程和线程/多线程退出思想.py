# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2512:13
# @Author  : 小符玩代码
# @Email   : 2737454073@qq.com
# @File    : 多线程退出思想.py
# @Software: PyCharm
import threading
import time
import os


# 原本需要用来启动的无线循环的函数
def print_thread():
    pid = os.getpid()
    counts = 0
    while True:
        print(f'threading pid: {pid} ran: {counts:04d} s')
        counts += 1
        time.sleep(1)


# 把函数放到改写到类的run方法中，便可以通过调用类方法，实现线程的终止
class StoppableThread(threading.Thread):

    def __init__(self, daemon=None):
        super(StoppableThread, self).__init__(daemon=daemon)
        self.__is_running = True
        self.daemon = daemon

    def terminate(self):
        self.__is_running = False

    def run(self):
        pid = os.getpid()
        counts = 0
        while self.__is_running:
            print(f'threading running: {pid} ran: {counts:04d} s')
            counts += 1
            time.sleep(1)


def call_thread():
    thread = StoppableThread()
    thread.daemon = True
    thread.start()

    pid = os.getpid()
    counts = 0
    for i in range(5):
        print(thread.isAlive())
        print(f'0 call threading pid: {pid} ran: {counts:04d} s')
        counts += 2
        time.sleep(2)
    # 主动把线程退出
    thread.terminate()


if __name__ == '__main__':
    call_thread()
    print(f'==========call_thread finish===========')
    counts = 0
    for i in range(5):
        counts += 1
        time.sleep(1)
        print(f'main thread:{counts:04d} s')

