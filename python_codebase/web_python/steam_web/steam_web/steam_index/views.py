import json
import requests
from django.shortcuts import render
from steam_index.models import steam
from django.core.paginator import Paginator
from django.http import JsonResponse


# Create your views here.
def index(request, pIndex=1):
    steanm = steam.objects.filter(appid='431960')
    # 执行分页
    pIndex = int(pIndex)
    Page = Paginator(steanm, 250)  # 以五条数据分页
    maxpages = Page.num_pages  # 获取最大页数
    # 判断是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list1 = Page.page(pIndex)  # 获取当前页面信息
    plist = Page.page_range  # 获取页码列表信息

    context = {'memberlist': list1, 'plist': plist, 'pindex': pIndex, 'maxpage': maxpages}

    return render(request, 'index.html', context)


def index2(request, pIndex=1):
    steanm = steam.objects.filter(appid='431960')
    # 执行分页
    pIndex = int(pIndex)
    Page = Paginator(steanm, 250)  # 以五条数据分页
    maxpages = Page.num_pages  # 获取最大页数
    # 判断是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list1 = Page.page(pIndex)  # 获取当前页面信息
    plist = Page.page_range  # 获取页码列表信息
    context = {'memberlist': list1, 'plist': plist, 'pindex': pIndex, 'maxpage': maxpages}

    return render(request, 'index.html', context)


def subscription(request):
    appid = request.GET.get('appid')
    publishedfileid = request.GET.get('publishedfileid')
    url = 'https://steamcommunity.com/sharedfiles/subscribe'
    head = {
        'Cookie': 'timezoneOffset=28800,0; _ga=GA1.2.940594228.1649389155; browserid=2541727184154055939; steamMachineAuth76561199034509976=D2F4E13358FCB45178EE065A0315FCA73696A33E; recentlyVisitedAppHubs=977950%2C431960; Steam_Language=schinese; steamLogin=76561199034509976%7c%7cCF71E77AD66F7C3BFBD5E926CD386C2E2F82EC8E; sessionid=bce6a38d246d86c9fca64356; steamLoginSecure=76561199034509976%7c%7c11930E28EF1218DD42FC41E2C4D38CD92F9A8BEB; clientsessionid=2dee100e0518bf2a; _gid=GA1.2.190111330.1658803513; app_impressions=431960@2_100100_100101_100103|431960@2_100100_100101_100103|431960@2_9_100000_|431960@2_9_100013_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_9_100000_|431960@2_9_100013_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_',
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.2; en-US; Valve Steam Client/default/1654574690; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }
    cookie = {}
    for i in head['Cookie'].split(';'):
        key,value = i.split('=', 1)
        cookie[key.strip()] = value.strip()
    data = {
        'sessionid': cookie['sessionid'],
        'id': publishedfileid,
        'appid': appid
    }
    response = requests.post(url, head, data,verify=False).json()

    return JsonResponse(response)
