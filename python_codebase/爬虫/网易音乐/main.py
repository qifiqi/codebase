import json
import time

import execjs
import requests


def decodeRES(a):
    js = execjs.compile(open("./d.js", encoding="utf-8").read())
    logid = js.call('getpwd', a)
    print(logid)
    return logid


headers = {
    "authority": "music.163.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://music.163.com/",
    "pragma": "no-cache",
    "referer": "https://music.163.com/",
    "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58"
}
cookies = {
    "vinfo_n_f_l_n3": "9124c2c29c190c24.1.1.1657536010620.1657536014769.1657536043477",
    "nts_mail_user": "xiaofu_base^@163.com:-1:1",
    "_ntes_nnid": "37cf8440b2dd90613b40805139c44bec,1678879839488",
    "WEVNSM": "1.0.0",
    "WNMCID": "gxsgla.1678879844328.01.0",
    "WM_TID": "m5KzQGLRbtRBUQAVEAeEaLw3UMZ7Frxt",
    "__bid_n": "1870d64adba32d49334207",
    "NMTID": "00OEdWDT-PME5AvsEdnvrsjEMpQQp4AAAGIKplmEA",
    "ntes_utid": "tid._.wxZtNUjVRZZEUkFRAAfE0U3dkoZ^%^252B6RU7._.0",
    "sDeviceId": "YD-H46A5CKGqk1AE1RQEUOFbGmmbtCY/gVQ",
    "FPTOKEN": "Q5cI0yZr55Yf4djKmlLOlP2AuFpMa2j3Rwm5CyKYplXMxfqP5Eb3YhFnLPffOWRprZDVworQV32AEtzwgPGkbZTPoNOXPIL3mn9EYNLFfJpQBXEaRvk7om4dCq3PA1Nd28HiUmcoHH9Q0tUHnUXps+uEmXWBA/CffYGoYx4H1xk8wR4hpXKplqNqR9IVbBw0xfuGJtdaAqkzQIR6EmOTX5XlIKC5HtkJ5hwxgwRjAPhxXQwKRKaZVGwfy2gCt66HhG6aSZdeiA3LX59OCdU62kPoNgnoiKYw2ADbuEfKfTkNjiPx9z7vIbqRStbWVnPQ8Lh6MV2dWTgO8F9OS+mtFCKVJAWIniXHONFmQdzUI0gb9UXRp1tLxQmpkpvq3+Kdzp/badFKQaQLBmPoCLR+vA==^|HvROSDDzIKTfEkOD9PsgT7dW7o9Qy1Vu6kCurdNTQAA=^|10^|ccaa506bd2acdd42b2336469da8313da",
    "NTES_P_UTID": "PhT3Gn9hXJawiJnwFgzuIEk5nleUo5Q2^|1688026052",
    "P_INFO": "xiaofu_base^@163.com^|1688026052^|0^|mail163^|00&99^|hun&1687972373&mailmaster_win^#hun&430900^#10^#0^#0^|176644&0^|mailmaster_win^|xiaofu_base^@163.com",
    "_iuqxldmzr_": "32",
    "WM_NI": "e6IiTWUknXlqXmujd^%^2BHBJCGzu5szkb7BToJl40^%^2F50QMO3aqqFny^%^2FFxazSoEK6babCa6JEzj5g7LhbHwVBYWzOYUDwDhkAwTw^%^2FWXZ452b^%^2F0Dd0Clg1bMibJYlvC2uAxlfVGo^%^3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6eed8e77b91afff99d23daeac8ea3d14f879e8ab0c87df3999796ce5992919b95d12af0fea7c3b92aa7ea878ad75d97b5a2b9ef7b9cb3bb8be7218c9e86a4c672b7ebbd9bea6af59e9c90c968f8f0e1d6b35b8f91fd82f47b86b2b7d0c574a3a69d90c841f6beaf83c26bf6968b9be93fa5e98489e144b58a8ebad6728d879ba5f650acb58f98d77ded8998bbb73ff2bee1d1c770f49da488b46a8fb7aeabdc68b69dfe96c474b0ba9aa8ee37e2a3",
    "playerid": "12165144",
    "JSESSIONID-WYYY": "VcFgDKPG8Tsll^%^2BhSYD^%^5CV4DI9CU0a0Beo8uh^%^2B6^%^2Fokzkk^%^5COTI5^%^5CoaoFeO26emfFD^%^5CH^%^2BTlXRbAGIoJKM9nBbVoy2AEJ8yNbWbls8u3TNQRgx90nU9hwipqU7djuENnnn^%^2FRKz^%^2Fq5^%^2BueMUwPI7YtP^%^2FMIugzVAiT9DqGsEljMvXIjEpjaaZCVp^%^3A1688112490879"
}
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
# t = int(time.time()*1000).__str__()

data = decodeRES(json.dumps(
    {
        "rid": "R_SO_4_28916645",
        "threadId": "R_SO_4_28916645",
        "pageNo": "2",
        "pageSize": "20",
        "cursor": "1676690370955",
        "offset": "0",
        "orderType": "1",
        "csrf_token": ""
    }
))
session = requests.session()
response = session.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
