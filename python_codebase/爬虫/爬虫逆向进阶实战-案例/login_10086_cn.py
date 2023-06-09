import base64
import time

import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def rsa_decode(data):
    key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsgDq4OqxuEisnk2F0EJFmw4xKa5IrcqEYHvqxPs2CHEg2kolhfWA2SjNuGAHxyDDE5MLtOvzuXjBx/5YJtc9zj2xR/0moesS+Vi/xtG1tkVaTCba+TV+Y5C61iyr3FGqr+KOD4/XECu0Xky1W9ZmmaFADmZi7+6gO9wjgVpU9aLcBcw/loHOeJrCqjp7pA98hRJRY+MML8MK15mnC4ebooOva+mJlstW6t/1lghR8WNV8cocxgcHHuXBxgns2MlACQbSdJ8c6Z3RQeRZBzyjfey6JCCfbEKouVrWIUuPphBL3OANfgp0B+QG31bapvePTfXU48TYK0M5kE+8LgbbWQIDAQAB'
    rsa_key = RSA.import_key(base64.b64decode(key))
    cipher = PKCS1_v1_5.new(rsa_key)
    cipher_text = base64.b64encode(cipher.encrypt(data.encode(encoding="utf-8")))
    return cipher_text.decode("utf-8")


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://login.10086.cn",
    "Referer": "https://login.10086.cn/html/login/email_login.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Google",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "^\\^Android^^"
}
cookies = {
    "sendflag": "20230609163511711776",
    "CaptchaCode": "BuNZBB",
    "rdmdmd5": "63C7A1126B4CEB07EE780791556FAADA"
}
aa_time = str(int(time.time() * 1000))
with open("aa.png", "wb+") as f:
    aa = requests.get(f'https://login.10086.cn/captchazh.htm?type=03&timestamp={aa_time}',
                      headers={
                          "GET": "/captchazh.htm?type=03&timestamp=1686300262296 HTTP/1.1",
                          "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                          "Accept-Encoding": "gzip, deflate, br",
                          "Accept-Language": "zh-CN,zh;q=0.9",
                          "Connection": "keep-alive",
                          "Cookie": "sendflag=20230609163511711776; CaptchaCode=IGQyXY",
                          "Host": "login.10086.cn",
                          "Referer": "https://login.10086.cn/html/login/email_login.html",
                          "Sec-Fetch-Dest": "image",
                          "Sec-Fetch-Mode": "no-cors",
                          "Sec-Fetch-Site": "same-origin",
                          "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
                          "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
                          "sec-ch-ua-mobile": "?1",
                          "sec-ch-ua-platform": "\"Android\""
                      }).content
    f.write(aa)
code = input("")
for i in range(len(code)+1):
    print(code[0:i])
    requests.get(f'https://login.10086.cn/verifyCaptcha?inputCode={code[0:i]}', headers={
        "GET": "/verifyCaptcha?inputCode=11 HTTP/1.1",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "sendflag=20230609163511711776; CaptchaCode=BuNZBB; rdmdmd5=63C7A1126B4CEB07EE780791556FAADA",
        "Host": "login.10086.cn",
        "Referer": "https://login.10086.cn/html/login/email_login.html",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\""
    })

url = "https://login.10086.cn/login.htm"
data = {
    "accountType": "02",
    "pwdType": "03",
    "account": rsa_decode("2737454073@qq.com"),
    "password": rsa_decode("123456"),
    "inputCode": code,
    "backUrl": "https://touch.10086.cn/i/",
    "rememberMe": "0",
    "channelID": "12014",
    "protocol": "https:",
    "loginMode": "03",
    "timestamp": aa_time
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)
