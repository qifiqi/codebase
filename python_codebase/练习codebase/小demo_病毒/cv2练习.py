# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/3118:56
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : cv2练习.py
__author__ = 'Small Fu'

import cv2
# 获取照相机
capo = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 读取相机当前是的图像内容 返回是否存在和图像的信息
ret, frame = capo.read()
# 保存图片
cv2.imwrite('./aa.png', frame)
# 关闭打开的摄像头
capo.release()
# 销毁打开的相机
cv2.destroyAllWindows()
