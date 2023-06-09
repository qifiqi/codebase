import requests
from

def rsa_decode():
    pass



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
    "sendflag": "20230609140557174860",
    "CaptchaCode": "BFNoRy"
}
url = "https://login.10086.cn/login.htm"
data = {
    "accountType": "02",
    "pwdType": "03",
    "account": "hgtmS4iSwNejGGgK2a1LdzI^%^2Bvw6fkjRp5obWuOK5nwf4U71^%^2F^%^2BEtHRc428fRS21eJz7a^%^2BQxgZ3xJwT1b1LTmavC0gzDiJEx6Qz882ML0Yr6^%^2BdUh0EuAjGaKbVHVRxACd67TypGgdfxs^%^2FgWeOxi^%^2FUDT4ynkDhUwFPzitfdC7LtHGPKeJmhd^%^2B7ggAznm4nn01MaY^%^2B43BgOrDoFtrBQs99^%^2FVsoUA5EujTDVQoN9TJML1epJoMwkGJ1b2x4kXJx6tmKPJKTqwQ1PdrghIoxsLki2wYqeQJ23gkJ2QkDVlsuIJK50uPuacT5iYi7Jl0dsTg^%^2FGDzxGoDG1Uhe961YEgAZEI4w^%^3D^%^3D",
    "password": "OP^%^2BcBxQTB1^%^2BEHpbvuphcMIl2s^%^2BpvokmOq6y30ZsZVkdK8xjMz6D2xuWTHNpVGDL6CiW9pSGWkUFp08zvJ4R2EE^%^2BthfbzRlqNWVH199oCy83UPG7hSORqJFyflh0Ne6yxocbkniRKzgORcc9rhNmOONTwnJ3YbGIQzA84eKImg9xHceBarombLlVl5FzbBk4Um^%^2FxNcn^%^2FpwlKvHXp2bJoMfsx6d0OFv5Igc4LenJHKONxFX9tyrK8nK6fMMQXRszwmTxi1U20wQAj8C8pozT^%^2BoydnTdTAY92X7w^%^2Fb3uLyjIpFxbszikgE3GcTATZBXGoz0Xn70UK9Gatypxx4lasM4Ag^%^3D^%^3D",
    "inputCode": "77",
    "backUrl": "https^%^3A^%^2F^%^2Ftouch.10086.cn^%^2Fi^%^2F",
    "rememberMe": "0",
    "channelID": "12014",
    "protocol": "https^%^3A",
    "loginMode": "03",
    "timestamp": "1686291261811"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)