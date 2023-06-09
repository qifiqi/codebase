# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/6/313:24
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : virustotal.com逆向案例.py
__author__ = 'Small Fu'

import requests
import execjs

def abuse_header():
    js = '''
    function computeAntiAbuseHeader() {
    const e = Date.now() / 1e3;
    return Buffer.from(`${(() => {
            const e = 1e10 * (1 + Math.random() % 5e4);
            return e < 50 ? "-1" : e.toFixed(0)
        }
    )()}-ZG9udCBiZSBldmls-${e}`).toString("base64")
}
    '''
    return execjs.compile(js).call('computeAntiAbuseHeader')




headers = {
    "authority": "www.virustotal.com",
    "accept": "application/json",
    "accept-ianguage": "en-US,en;q=0.9,es;q=0.8",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "referer": "https://www.virustotal.com/",
    "sec-ch-ua": "^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "x-app-version": "v1x183x6",
    "x-tool": "vt-ui-main",
    "x-vt-anti-abuse-header": abuse_header()
}
cookies = {
    "_ga_BLNDV9X2JR": "GS1.1.1685769658.1.0.1685769658.0.0.0",
    "_ga": "GA1.2.141283236.1685769659",
    "_gid": "GA1.2.1440628198.1685769659",
    "_gat": "1"
}
url = "https://www.virustotal.com/ui/search"
params = {
    "limit": "20",
    "relationships^%^5Bcomment^%^5D": "author^%^2Citem",
    "query": "1"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)
