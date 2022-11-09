# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/916:02
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : 读取表格文本.py
__author__ = 'Small Fu'

from docx import Document
doc = Document("路径")
all_tables = doc.tables
for tables in all_tables:
    for row in tables.rows:
        for cell in row.cells:
            print(cell.text)