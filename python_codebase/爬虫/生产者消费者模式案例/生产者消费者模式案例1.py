import requests
import threading
from queue import Queue
import time


# 生产者只请求页面
class MyProducer(threading.Thread):
    def __init__(self, i, page_queue):
        super().__init__()
        self.i = i
        self.page_queue = page_queue

    # 复写run方法
    def run(self):
        # 任务队列不为空就取数据执行
        while True:
            if self.page_queue.empty():
                break
            try:
                q = self.page_queue.get(block=False)
                print(self.i, '开始任务%s=======' % (q))
                url = 'https://careers.tencent.com/tencentcareer/api/post/Query?keyword=python&pageIndex=%s&pageSize=10' % (
                    q)
                self.getHtml(url)
                print(self.i, '结束任务=======')
            except:
                pass

    def getHtml(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        response = requests.get(url=url, headers=headers).json()
        response_q.put(response)


class MyCousumer(threading.Thread):
    def __init__(self, i):
        super().__init__()
        self.i = i

    # 复写run方法
    def run(self):
        # 任务队列不为空就取数据执行
        while True:
            # 1.任务队列为空，2生产者进程全部结束
            if response_q.empty() and flag:
                break

            try:
                response = response_q.get(block=False)
                self.parse_html(response)
            except:
                pass

    def parse_html(self, response):
        job_lst = response['Data']['Posts']
        for job in job_lst:
            name = job['RecruitPostName']
            address = job['LocationName']
            Responsibility = job['Responsibility']
            Responsibility = Responsibility.replace('\n', '').replace('\r', '')
            PostURL = job['PostURL']

            info = "工作名称：%s,工作地点：%s，岗位职责：%s，详情：%s" % (name, address, Responsibility, PostURL)

            # 加锁
            with lock:
                with open("腾讯招聘.txt", 'a', encoding='utf-8') as f:
                    f.write(info + '\n')


lock = threading.Lock()  # 锁
response_q = Queue()  # 消费者队列
flag = False  # 表示生产者线程是否都结束
if __name__ == '__main__':
    # 创建生产者任务队列
    page_queue = Queue()
    for i in range(1, 88):
        page_queue.put(i)

    # 启线程队列
    producer_name = ['p1', 'p2', 'p3']
    p_tread = []
    cousumer_name = ['c1', 'c2', 'c3']
    c_tread = []

    # 启动三个生产者线程
    for i in producer_name:
        p_crawl = MyProducer(i, page_queue)
        p_crawl.start()
        p_tread.append(p_crawl)

    # 启动三个消费者线程
    for j in cousumer_name:
        c_crawl = MyCousumer(j)
        c_crawl.start()
        c_tread.append(c_crawl)

    # 生产者阻塞主线程
    for threadi in p_tread:
        threadi.join()
    # 生产者都死了把flag变成True，可以让消费者做判断
    flag = True

    # 消费者阻塞主线程
    for threadi in c_tread:
        threadi.join()
