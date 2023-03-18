import json
import random
import time
import requests
import datetime

urls = 'https://api.xixunyun.com/Reports/StudentOperator?token=d6af8dac84d3b97a7e9b5dedcd5b007f'


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


def weekRange(beginDate, endDate):
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


def encode_data(da, bu="week", days=7):
    '''
    返回周data
    :param da:
    :return:
    '''
    start_date = datetime.datetime.strptime(da, "%Y-%m-%d")
    stop_date = (start_date + datetime.timedelta(days=days)).strftime("%Y/%m/%d")

    context_2 = '完成本周分配项目的书写，完成相关的爬虫项目解析器的书写' + str(
        random.randint(6 * 6, 6 * 9)) + '个，修改相关的项目解析器' + str(random.randint(6 * 3, 6 * 5)) + '个'
    context_1 = "完成本周工作，并参加对应会议报告工人详情，" + context_2

    data = {
        'business_type': bu,  # week ,month
        'start_date': start_date.strftime("%Y/%m/%d"),
        'end_date': stop_date,
        'content': [
            {"title": "实习工作具体情况及实习任务完成情况", "content": context_1, "require": "1", "sort": 1},
            {"title": "主要收获及工作成绩", "content": context_2, "require": "0", "sort": 2},
            {"title": "工作中的问题及需要老师的指导帮助", "content": "", "require": "0", "sort": 3}],
        'attachment': '',
    }
    data['content'] = json.dumps(data["content"])
    return data


def weekly_push():
    for da in weekRange('2022-12-12', '2023-6-12')[:22]:
        data = encode_data(da)
        headers = {
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
        }

        response = requests.post(urls, headers=headers, data=data)
        print(response.json())
        print(response.status_code)
        time.sleep(3)


def uploadMonthlyReport():
    '''

    :return:
    '''

    for da in range(1, 6):
        da = f"2023-{da}-1"
        data = encode_data(da, bu='month', days=22)

        data['content'] = json.dumps(
            [{"title": "实习工作具体情况及实习任务完成情况", "content": "完成本月相关工作，并学习相关的项目结构",
              "require": "1",
              "sort": 1},
             {"title": "主要收获及工作成绩", "content": "完成本月相关工作，并学习相关的项目结构", "require": "0",
              "sort": 2},
             {"title": "工作中的问题及需要老师的指导帮助", "content": "", "require": "0", "sort": 3}])

        headers = {
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
        }

        response = requests.post(urls, headers=headers, data=data)
        print(response.json())
        print(response.status_code)
        time.sleep(3)
uploadMonthlyReport()