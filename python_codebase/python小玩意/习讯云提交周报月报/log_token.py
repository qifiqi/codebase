# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/5/518:06
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : log_token.py
__author__ = 'Small Fu'

import DA
import base64
from DA import SESSIONS


def j_data_encode():
    j_data = DA.USER + ";"
    j_data += DA.PASSWORD + ";"
    j_data += '1'

    return base64.b64encode(j_data.encode("utf-8")).decode("utf-8")


def login_token():
    data = {
        "school_id": "542",
        "j_data": j_data_encode(),
        "type": "web",
        "alg": "en001"
    }
    SESSIONS.post()
