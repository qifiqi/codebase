# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/11/1015:50
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : temp_1.py
__author__ = 'Small Fu'

from django import template
from app01 import models
from django.db.models.functions import TruncMonth
from django.db.models import Count



register = template.Library()


# 自定义inclusion_tag
@register.inclusion_tag("left_menu.html")
def left_menu(username):
    # 构造侧边栏需要的数据

    user_obj = models.UserInfo.objects.filter(username=username).first()
    blog = user_obj.blog
    # 1.查询当前用户所有的分类及分类小的文章数
    category_list = models.Category.objects.filter(blog=blog).annotate(
        count_name=Count("article__pk")
    ).values("pk", "name", "count_name")

    # 2.差早当前用户所有的标签和标签数
    tag_list = models.Tag.objects.filter(blog=blog).annotate(
        count_name=Count("article__pk")
    ).values("pk", "name", "count_name")

    # 3.更加年月份分组统计
    data_list = models.Article.objects.filter(blog=blog).annotate(
        month=TruncMonth("create_time")).values("month").annotate(
        count_name=Count("pk")).values("month", "count_name")

    return locals()