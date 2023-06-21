# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/8/1420:12
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : a.py
__author__ = 'Small Fu'



class a:
    def __init__(self,num=[]):
        self.num = num


    def set(self,a):
        self.num.append(a)

    def pr(self):
        return self.num

    # def __str__(self):
    #     return self.num

if __name__ == '__main__':
    a1 = a()
    a2 = a()

    a1.set(1)
    a2.set(2)

    print(a1.pr())
    print(a2.pr())
