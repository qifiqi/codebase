# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/718:30
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : login_hodj.py
__author__ = 'Small Fu'

import hashlib
import json
import requests
import time

"""
 https://user.hrdjyun.com/wechat/phonePwdLogin
 登录模块
 {"phoneNum":"17670344644","pwd":"b6d54030e1314d6716a52a0342a2f001","t":1665138632573,"tenant":1,"sig":"00d7064abcf1be94514eccdd3426c3e7"}
 
 """

seeeion = requests.session()
seeeion.headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Length": "137",
    "Content-Type": "application/json",
    "Host": "user.hrdjyun.com",
    "Origin": "http://www.hrdatayun.com",
    "Referer": "http://www.hrdatayun.com/",
    "sec-ch-ua": '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34",
}
token = open('static/红人点集_token', 'r', encoding="utf-8").read().strip()


def md5_encode(content: str) -> str:
    """
    调试得知加密是MD5加密，密码和sig参数但是MD5加密
    :param content: 密码或者加密的字符串
    :return: 加密后的数据
    """
    md5 = hashlib.md5()
    md5.update(content.encode("utf-8"))
    return md5.hexdigest()


def get_log() -> token:
    """
    登录函数，用于获取token参数
    """
    data = {
        "phoneNum": "17670344644",
        "pwd": md5_encode("2002308FUqing"),
        "t": str(int(time.time() * 1000)),
        "tenant": 1,
        "sig": "00d7064abcf1be94514eccdd3426c3e7"
    }
    strs = data.get("phoneNum") + data.get("pwd") + data.get("t") + "1" + "JzyqgcoojMiQNuQoTlbR5EBT8TsqzJ"
    data["sig"] = md5_encode(strs)
    url = "https://user.hrdjyun.com/wechat/phonePwdLogin"
    res_json = seeeion.post(url, json.dumps(data)).json()

    if res_json.get('status') == 0:
        global token
        token = res_json.get("data").get("token")
        with open('static/红人点集_token', "w", encoding="utf-8") as t:
            t.write(token)
            t.close()
        print(token)


if __name__ == '__main__':
    get_log()
