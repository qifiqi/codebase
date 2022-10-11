import csv, time, sys, signal

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def sele_dy(url):
    driver = webdriver.Chrome(r"D:\专业\python数据\static\chromedriver.exe")
    # 打开页面
    # driver.get('https://live.douyin.com/777528469683')
    driver.get(url)
    lis = []
    time.sleep(5)
    while True:
        try:
            text_pinglun = {}
            html = driver.page_source

            html = etree.HTML(html)
            # print(html)
            a = html.xpath('//div[@class="webcast-chatroom___items"]/div/div')
            time.sleep(0.5)
            for i in range(1, len(a)):
                text = a[i].xpath('.//div/span[3]/span/text()')

                text1 = text[0]
                id = a[i].xpath('./@data-id')
                id1 = id[0]

                if id1 in lis:
                    # text_pinglun[id1]=text1
                    pass
                else:
                    print(id1, ":", text1)
                    lis.append(id1)
                    if len(lis) > 100:
                        del (lis[0])

        except Exception as a:
            print(a)
            continue


if __name__ == '__main__':
    sele_dy("https://live.douyin.com/777528469683")
# for key,value in text_pinglun.items():
#     print(key,":",value)
