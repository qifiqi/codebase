# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2723:45
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : run.py
# @Software: PyCharm
__author__ = 'Small Fu'

import re
import requests
from lxml import etree
import json
import os.path
import sys

# from concurrent.futures import ProcessPoolExecutor

from core import fyxfcw_text, Crawl_articles_list

sys.path.append(os.path.dirname(__file__))

if __name__ == '__main__':
    # Crawl_articles_list.articles_list()
    # for i in json.loads(open('./articles/玄幻奇幻.json', 'r', encoding='utf-8').read()):
    #     url = 'https://www.fyxfcw.com' + i.get('text_href')
    #     print(i.get('text'))
    #     print(url)
    # fyxfcw_text.main(url=url, types='玄幻奇幻')
    url = 'https://www.fyxfcw.com/book/73623/'
    fyxfcw_text.main(url=url, types='玄幻奇幻')
    # main(urls)
