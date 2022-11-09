# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/1220:28
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : url_encode.py
__author__ = 'Small Fu'

import base64
def url_encode():
    t = "pX7rCko1ZPLJXbyU3qjcDqAp042BK5yCrhhNlUZEBd6lHKILemhbvHD1YkhQ7FDbfVGHk5B7R7MisliWsBq3R_koq_gN4bHRxtddpUQwGn30cliBte8fftHC_vHfQSLbPnY_QkRExN9aRxgM9IaQ-ZNlqANOCGG-yj5A_dcFsn-8RjYxJQRD_xXOOq46qUsPNYwjKQsB-8gMzYFidbprSbmnhudvW2OVkqiF7LyW0Jk1NXJpDc2o3_bVkQddNf-5CfKCTKjhG0vllzgBORsDTc2lcxIACl1qGf-DYqhMORFDwnANT6bI8NuNqO6XreSTIQeOfNXxLlvXexErOExBGw".encode()
    res = base64.b64decode(t)
    print(res.decode())

url_encode()