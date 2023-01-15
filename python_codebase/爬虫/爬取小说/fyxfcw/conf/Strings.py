# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2723:38
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : Strings.py
# @Software: PyCharm
__author__ = 'Small Fu'

import os.path
from lib import module_fyxfcw

USER_AGENT_LIST = module_fyxfcw.user_agent_list()

"""类型匹配"""
ARTICLES_TYPE_DICT = {
    '1': '玄幻奇幻',
    '2': '武侠仙侠',
    '3': '都市言情',
    '4': '历史军事',
    '5': '科幻灵异',
    '6': '网游竞技',
    '7': '女生频道',
}

"""项目路径"""
PROJECT_DIRECTORY = os.path.dirname(
    os.path.dirname(__file__)
)

"""资源文件夹"""
ARTICLES_DIR = os.path.join(PROJECT_DIRECTORY, 'articles')

"""添加最大生产者进程数"""
PRODUCER_THREADING_MAX = 64

"""添加最大消费者进程数"""
CONSUMER_THREADING_MAX = 3

"""线程池最大线程数"""
THREADPOOLEXECUTOR_MAX = 10
