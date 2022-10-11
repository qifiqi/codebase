# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/21 14:23
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : zh_CN_oil.py
# @Software: PyCharm
import json
import sys
import pymysql
import requests
import threading
import queue
from threading import Lock
from time import sleep
from faker import Faker

res_queue = queue.Queue()
data_queue = queue.Queue()
lock = Lock()
exit_c = False
file_json = open('zh_CN_oil.json', 'w', encoding='utf-8')
fa = Faker('zh_CN')
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123123',
    db='text_db',
)
cursor = conn.cursor()


def db_exits():
    sql = '''
        create table if not exists zh_CN_oil(
    id varchar(40) primary key not null comment 'id',
    names varchar(200) not null comment '投标公司',
    times datetime not null comment '投标时间'
)
    '''
    cursor.execute(sql)
    conn.commit()


def requests_oil():
    while True:
        if res_queue.empty():
            break
        url = 'https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut'
        header = {
            'Host': 'www.cnpcbidding.com',
            'Content-Length': '121',
            'Content-Type': 'application/json;charsetset=UTF-8',
            'User-Agent': fa.chrome(),
            'Referer': 'https://www.cnpcbidding.com/html/1/index.html',

        }
        id = res_queue.get()
        datas = json.dumps(
            {"url": "./list.html", "pid": "180", "pageSize": 15, "categoryId": "201", "title": "", "projectType": "",
             "pageNo": id, "shiXinName": ""})
        data_json = requests.post(url=url, headers=header, data=datas).json()
        data_queue.put(data_json)


def response_json():
    while True:
        if data_queue.empty() and exit_c:
            break
        data_json = data_queue.get()
        data_list = data_json['list']
        with lock:
            for i in data_list:
                j = json.dumps({
                    'id': i['id'],
                    'projectname': i['projectname'],
                    'dateTime': i['dateTime']
                }, ensure_ascii=False)
                print(j)
                file_json.write(j + '\n')
                sql = 'INSERT INTO zh_cn_oil VALUES (%s,%s, %s)'
                cursor.execute(sql, (i['id'], i['projectname'], i['dateTime']))
            else:
                conn.commit()


def coles():
    cursor.close()
    conn.close()
    file_json.close()
    print("结束")
    sys.exit()


if __name__ == '__main__':
    db_exits()

    for i in range(1, 6):
        res_queue.put(i)

    # 生产者队列
    producer_threading = [' producer1', ' producer2']
    producer_threading_list = []
    # 消费者队列
    consumer_threading = ['consumer1']
    consumer_threading_list = []

    # 产生生产者
    for i in producer_threading:
        p_crawl = threading.Thread(target=requests_oil, name=i)
        p_crawl.start()
        producer_threading_list.append(p_crawl)
    sleep(1)  # 等待队列中有数据再去消费
    # 产生消费者
    for i in consumer_threading:
        c_crawl = threading.Thread(target=response_json, name=i)
        c_crawl.start()
        consumer_threading_list.append(c_crawl)
    # 设置生产者阻塞
    for i in producer_threading_list:
        i.join()

    exit_c = True  # 用于关闭

    # 设置消费者阻塞
    for i in consumer_threading_list:
        i.join()

    coles()
