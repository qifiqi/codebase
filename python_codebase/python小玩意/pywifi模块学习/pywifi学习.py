# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/26 23:43
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : pywifi学习.py
# @Software: PyCharm
import pprint
import time

import pywifi
from pywifi import const, profile

wifi = pywifi.PyWiFi()  # 获取
inter = wifi.interfaces()[0]

inter.scan()
time.sleep(2)
for i in inter.scan_results():
    print(i.ssid.encode('raw_unicode_escape', 'strict').decode())
