# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/1313:31
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : mtalk.py
__author__ = 'Small Fu'

import json
import pprint
import redis
import requests

"""

https://www.1905.com/mtalk/


https://www.1905.com/api/content/?callback=reloadList&m=converged&a=info&type=jryp&year=2022&month=9


Referer: https://www.1905.com/mtalk/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
Cookie: pvid=1665639103782; __uv_=8857003174; WOlTvIlgRpuvid_=1331; WOlTvIlgRptime_=1665639103782; SpMLdaPxuv=m7086353402; Hm_lvt_49411f7bde52035653f2e2b70a0bb6a5=1665639104; Hm_lpvt_49411f7bde52035653f2e2b70a0bb6a5=1665639104; Hm_lvt_5a9573957327e40b58294447cd1d8ad2=1665639104; Hm_lpvt_5a9573957327e40b58294447cd1d8ad2=1665639104; PHPSESSID=qsjhi7hgsr2qi84q30vc2g20j7


"""

red = redis.Redis(
    host="192.168.110.141",
    port=6379,
    password="123qweasd",
    decode_responses=True,  # 改成字符串简单来说就是设置中文显示
    # charset="UTF-8",
    # encoding="UTF-8",
    db=2,  # 指定数据库
)
print(red.keys())



head = {
    "Referer": "https://www.1905.com/mtalk/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
}


def get_content(year: str = '2022', month: str = "9"):
    url = f"https://www.1905.com/api/content/?callback=reloadList&m=converged&a=info&type=jryp&year={year}&month={month}"
    response = requests.get(url, headers=head).text
    response = response.replace("reloadList(", "")[:-1]
    try:
        res_json = json.loads(response)
    except Exception as exc:
        print(exc)

    # json 格式保存
    aa = {}
    date = "-".join((year, month))
    aa[date] = {
        "info": res_json.get("info"),
        "jckdvideos": res_json.get("jckdvideos")
    }

    # 输出，然后扔到保存文件中
    print(date)
    set_file(aa, date)


def set_file(res_json, date):
    # 先读取
    res_json_file = open("./1905_电影评论.json", "r", encoding="utf-8")
    json_file = json.loads(res_json_file.read())
    res_json_file.close()
    # 保存
    json_file[date] = res_json.get(date)
    red.hset("1905", str(date), json.dumps(res_json.get(date), ensure_ascii=False))
    with open("./1905_电影评论.json", "w+", encoding="utf-8") as f:
        f.write(json.dumps(json_file, ensure_ascii=False))


def main():
    # year = input("输入年份:").zfill(4)
    # month = input("输入月份:").zfill(2)
    for i in range(1, 13):
        get_content("2021", str(i))

    for i in range(1, 10):
        get_content("2022", str(i))


if __name__ == '__main__':
    main()
    # get_content("2022","1")
    red.close()
