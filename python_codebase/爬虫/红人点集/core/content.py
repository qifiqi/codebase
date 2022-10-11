# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/719:55
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : content.py
__author__ = 'Small Fu'

import hashlib
import json
import pprint
import time
from core.login_hodj import *

"""
这个模块用于数据采集
"""


def sign_get(strs: str) -> str:
    """
    经过调试分析得出
        这个网站的sign参数是通过sha256加密的
    :param strs: 拼接的字符串
    :return: 返回加密的字符串
    """
    sha = hashlib.sha256()
    sha.update(strs.encode('utf-8'))
    return sha.hexdigest()


def get_Data(param: dict) -> json:
    """
    用于对"https://ucp.hrdjyun.com:60359/api/dy"地址进行请求获取数据
        这个地址的数据是通过param参数改变的
    :param param: 传入的字典，其中包含数据的类型等
    :return: 返回接口返回的json文件
    """
    url = "https://ucp.hrdjyun.com:60359/api/dy"
    params = json.dumps(param)
    data = {"param":
                params,
            "sign": "",
            "tenant": "1",
            "timestamp": int(time.time() * 1000),
            "token": token
            }
    sign_str = "param=" + params + \
               "&timestamp=" + str(data.get("timestamp")) + \
               "&tenant=1&salt=" + "kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$"
    data['sign'] = sign_get(sign_str)
    response = seeeion.post(url, json.dumps(data), timeout=5)
    try:
        response = response.json()

    except Exception as ee:
        print(ee)
    static = response.get("status")
    if static == 0:
        return response
    elif static == 2:
        time.sleep(2)
        get_log()
        get_Data(param)
    else:
        return "no"

