# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/822:59
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : urls.py
__author__ = 'Small Fu'
from django.urls import path
from app1 import views



urlpatterns = [
    path('',views.index,name="app1_index")
]
