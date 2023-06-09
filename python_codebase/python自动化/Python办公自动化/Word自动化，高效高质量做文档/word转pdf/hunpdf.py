# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/916:37
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : hunpdf.py
__author__ = 'Small Fu'

from win32com.client import Dispatch, constants, gencache

docx_path = "./客户0-价格通知.docx"
pdf_path = "./a.pdf"

gencache.EnsureModule("{00020905-0000-0000-C000-000000000046}", 0, 8, 4)
wd = Dispatch('Word.Application')
doc = wd.Documents.Open(docx_path,ReadOnly=1)

doc.ExportAsFixedFormet(pdf_path,constants.wdExportFormetPDF,I)