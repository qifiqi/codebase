# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/9/2122:26
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : dow.py
__author__ = 'Small Fu'

import json
import os
import time

import aligo
import subprocess

import logging
from aligo.types import EMailConfig

aligo_clise = aligo.Aligo(
    email=EMailConfig(
        email='2737454073@qq.com',
        host='smtp.163.com',
        port=465,
        user='xiaofu_base@163.com',
        password='OYSHQLSAGFDLZXIF',
    )
)
# f_aa = open("./aa.txt", 'a+', encoding="utf-8")


def dow(url, name, id):
    aa = subprocess.call(f"./ffmpeg-N-112136-g33b2646d61-win64-gpl/bin/ffmpeg.exe -i {url} {id}.mp4")


def pull_aligo(path):
    aligo_clise.upload_file(
        file_path=path,
        parent_file_id='650c5752bd25ade7c4a349eca9d0cafbe03ed1de',
        name=path.split('/')[-1],
        check_name_mode='refuse'
    )



def main(item):
    data = json.loads(item)
    id = data["data-video-id"]
    m3u8 = data["mp4_url_m3u8"]
    title = data["data-video-title"]
    dow(url=m3u8, name=title, id=id)
    pull_aligo(path=f"{id}.mp4")
    time.sleep(5)
    os.remove(f"{id}.mp4")
    print(f"{id}.mp4 删除")



if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor, as_completed

    # with open("./url.json",'r',encoding="utf-8") as f:
    #     with ThreadPoolExecutor(max_workers=5) as pool:
    #         for item in f.readlines():
    #             # main(item)
    #             pool.submit(main,item)

    # max_pool = 5	# 线程池最大线程数
    # executor = ThreadPoolExecutor(max_pool)
    # all_task = []
    # with open("./url.json",'r',encoding="utf-8") as f:
    #     for item in f.readlines():
    #         if len(all_task) < max_pool:
    #             all_task.append(executor.submit(main, item))
    #         else:
    #             for future in as_completed(all_task):
    #                 all_task.remove(future)
    #                 all_task.append(executor.submit(main, item))
    #                 break
    #     for future in as_completed(all_task):
    #         print('完成：', future.result())

    # logging.info(f"{item}开始解析")
    # data = json.loads(item)
    # id = data["data-video-id"]
    # m3u8 = data["mp4_url_m3u8"]
    # title = data["data-video-title"]
    # dow(url=m3u8, name=title, id=id)
    # pull_aligo(path=f"{id}.mp4")
    # setfile(content=f"{id}{title}\n")
    # os.remove(f"{id}.mp4")
    # logging.info(f"{id}.mp4 删除")
    # logging.info(f"{id}解析完成")

    # id_list = []
    # # for i in aligo_clise.get_file_list(parent_file_id='650c5746e31174aff80948b0a7e44c4936a9db72'):
    # aa = aligo_clise.get_file_list(parent_file_id='650c5752bd25ade7c4a349eca9d0cafbe03ed1de')
    # for i in aa:
    #     if '(' in i.name:
    #         print(i)
    #     id_list.append(i.name.strip('.mp4'))
    # print(id_list)
    # # pull_aligo('v20230921_213624.json')
    # fil = open("./url.json", 'w', encoding='utf-8')
    # for i in open("./v20230921_213624.json", 'r', encoding='utf-8').readlines():
    #     data = json.loads(i.strip())
    #     id = data['data-video-id']
    #     if id in id_list:
    #         continue
    #     fil.write(i)
