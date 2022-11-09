# -*- coding: utf-8 -*-
# All Rights Reserved
# @Time    : 2022/10/915:54
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : 读取简单word纯文本.py
__author__ = 'Small Fu'

from docx import Document

doc = Document("地址.docx")
all_paragraphs = doc.paragraphs # 读取所有的段落
for paragraphs in all_paragraphs:
    print(paragraphs.text)
