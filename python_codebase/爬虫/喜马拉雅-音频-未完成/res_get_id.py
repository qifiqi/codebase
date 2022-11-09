# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/10/1213:26
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : res_get_id.py
__author__ = 'Small Fu'

import hashlib
import pprint
import random
import time

import requests

head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37",
    "referer": "https://www.ximalaya.com/album/54079657",
}
# head["cookie"] = "_xmLog=h5&f5662cff-c624-4f60-a7e2-2dd4ff842c5f&process.env.sdkVersion; xm-page-viewid=ximalaya-web; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1665551873; trackType=web; 1&remember_me=y; 1&_token=219316279&E2090B90140NCBA1B0CA2ECF08798B2D91B0189141E0A74F9C69C6A70D07A08CFE4E0A087A25168M16F98D76F2FFCF5_; 1_l_flag=219316279&E2090B90140NCBA1B0CA2ECF08798B2D91B0189141E0A74F9C69C6A70D07A08CFE4E0A087A25168M16F98D76F2FFCF5__2022-10-1213:18:00; x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A; web_login=1665552404505; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1665552405"


def xm_sign():
    # "{himalaya-1665553001695" + "}(0)" + e + "(" + u(100) + ")" + r
    f_times = requests.get("https://www.ximalaya.com/revision/time", headers=head).text
    now_times = str(int(time.time() * 1000))
    m = hashlib.md5()
    m.update(f"himalaya-{f_times}".encode("utf-8"))
    s = str(m.hexdigest()) + f"({str(random.randint(0, 100))})" + str(
        f_times) + f"({str(random.randint(0, 100))})" + str(now_times)
    head["xm-sign"] = s


def getTracksList(albumId="54079657", pageNum="1"):
    xm_sign()
    url = f"https://www.ximalaya.com/revision/album/v1/getTracksList?albumId={albumId}&pageNum={pageNum}"
    res_ks = requests.get(url, headers=head).json()
    tracks = res_ks.get("data").get("tracks")
    pprint.pp(tracks)

def baseInfo(trackId=482666473):
    url = f"https://mobile.ximalaya.com/mobile-playpage/track/v3/baseInfo/{str(int(time.time()*1000))}?device=web&trackId={trackId}&trackQualityLevel=1"
    res = requests.get(url,headers=head).json()
    pprint.pp(res)


baseInfo()