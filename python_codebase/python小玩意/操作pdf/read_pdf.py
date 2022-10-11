# -*- coding: utf-8 -*-
import pdfplumber
with pdfplumber.open("./英语词汇汇总.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()#提取文本
        print(text)