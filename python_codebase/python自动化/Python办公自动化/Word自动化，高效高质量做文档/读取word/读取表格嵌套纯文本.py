# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/916:06
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : 读取表格嵌套纯文本.py
__author__ = 'Small Fu'
import zipfile

word = zipfile.ZipFile("路径")
xml = word.read("word/document.xml").decode('utf-8')

xml_list = xml.split("<w:t>")
text_file = []
for xml in xml_list:
    if xml.find("</w:t>")+1:
        text_file.append(
            xml[:xml.find("</w:t>")]
        )
    else:
        pass
text_file = "".join(text_file)





