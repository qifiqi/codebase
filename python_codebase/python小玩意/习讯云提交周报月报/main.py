import json
import random
import time
import requests
from datetime import datetime, date

# 这里吧这个token改一下登录这个网站拿
# https://www.xixunyun.com/
urls = 'https://api.xixunyun.com/Reports/StudentOperator?token=8c6dad6cfc8c6f06505fad815cabbd06'

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-length": "868",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.xixunyun.com",
    "pragma": "no-cache",
    "referer": "https://www.xixunyun.com/",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Microsoft Edge\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68"
}


def dateRange(beginDate, endDate):
    '''
    获取时间段内所有天
    :param beginDate:
    :param endDate:
    :return:
    '''
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates


def get_current_week(x_time):
    import datetime
    '''
    求本周的星期一

    :param x_time:
    :return:
    '''
    monday = datetime.datetime.strptime(x_time, "%Y-%m-%d")
    one_day = datetime.timedelta(days=1)
    while monday.weekday() != 0:
        monday -= one_day
    return monday.strftime('%Y-%m-%d')


def encode_data(da, context_1, context_2, context_3, bu="week", days=7):
    import datetime
    '''
    返回周和月的data,自己改，
    start_data是起始时间
    end_data是结束时间
    content：是具体内容只要改title和content就好
    :param da:
    :return:
    '''
    start_date = datetime.datetime.strptime(da, "%Y-%m-%d")
    stop_date = (start_date + datetime.timedelta(days=days)).strftime("%Y/%m/%d")

    data = {
        'business_type': bu,  # week ,month
        'start_date': start_date.strftime("%Y/%m/%d"),
        'end_date': stop_date,
        'content': [
            {"title": "实习工作具体情况及实习任务完成情况", "content": context_1, "require": "1", "sort": 1},
            {"title": "主要收获及工作成绩", "content": context_2, "require": "0", "sort": 2},
            {"title": "工作中的问题及需要老师的指导帮助", "content": context_3, "require": "0", "sort": 3}],
        'attachment': '',
    }
    data['content'] = json.dumps(data["content"])
    return data


def weekRange(beginDate, endDate):
    import datetime
    '''
    时间段内每个星期的周一日期

    :param beginDate:
    :param endDate:
    :return:
    '''
    date_week = []
    date_list = dateRange(beginDate, endDate)
    for i in date_list:
        dt = datetime.datetime.strptime(i, "%Y-%m-%d")
        if dt.weekday() == 0:
            date_week.append(i)
    if date_week[0] != date_list[0]:
        date_week.insert(0, get_current_week(date_list[0]))

    return date_week


def dateRange(beginDate, endDate):
    import datetime
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates


def weekly_push():
    """
    这里是推周报 自己改时间
    :return:
    """

    for da in weekRange('2022-04-01', '2023-04-30'):
        data = encode_data(da, '检测每日是否存在安全问题', '可以收获以前没有的信心', '有一些标签不懂')

        response = requests.post(urls, headers=headers, data=data)
        print(response.json())
        print(response.status_code)
        time.sleep(3)


def uploadMonthlyReport():
    '''
    这里是月报
    :return:
    '''

    for da in range(1, 4):
        da = f"2023-{da}-1"
        data = encode_data(da, "", "", "", bu='month', days=22)

        data['content'] = json.dumps(
            [
                {"title": "实习工作具体情况及实习任务完成情况", "content": '检测每日是否存在安全问题        ',
                 "require": "1", "sort": 1},
                {"title": "主要收获及工作成绩", "content": '可以收获以前没有的信心', "require": "0", "sort": 2},
                {"title": "工作中的问题及需要老师的指导帮助", "content": "有一些标签不懂", "require": "0", "sort": 3}
            ])

        response = requests.post(urls, headers=headers, data=data)
        print(response.json())
        print(response.status_code)
        time.sleep(3)


def day_put():
    """
    这里是日报同上
    :return:
    """
    pass
    for i in dateRange('2022-04-01', '2023-04-30'):
        if datetime.strptime(i, "%Y-%m-%d").strftime("%A") in ['Saturday', 'Sunday']:
            continue
        i = datetime.strptime(i, "%Y-%m-%d").strftime("%Y/%m/%d")

        data = {
            'business_type': 'day',  # week ,month
            'start_date': i,
            'end_date': i,
            'content': [
                {"title": "实习工作具体情况及实习任务完成情况", "content": '检测每日是否存在安全问题        ',
                 "require": "1", "sort": 1},
                {"title": "主要收获及工作成绩", "content": '可以收获以前没有的信心', "require": "0", "sort": 2},
                {"title": "工作中的问题及需要老师的指导帮助", "content": "有一些标签不懂", "require": "0", "sort": 3}],
            'attachment': '',
        }
        data['content'] = json.dumps(data["content"])
        response = requests.post(urls, headers=headers, data=data)
        print(response.json())
        print(response.status_code)
        time.sleep(3)


# weekly_push()
# uploadMonthlyReport()
day_put()
