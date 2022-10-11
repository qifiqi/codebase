import requests  # 导入网页请求模块
from lxml import etree  # 导入解析模块
import threading  # 导入线程模块
from queue import Queue  # 导入队列模块
import time
from urllib import request  # 导入网页请求、下载模块
import os  # 导入文件操作模块


# 继承父类threading.Thread
class AutoHomeThread(threading.Thread):
    headers = {
        'User-Agent': '***********************************',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Host': 'car.autohome.com.cn',
        'Cookie': '**************************************'
    }

    def __init__(self, page_queue, detail_queue, *args, **kwargs):
        # 增加父类的属性
        super(AutoHomeThread, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.detail_queue = detail_queue
        self.base_domain = "https://club.autohome.com.cn"
        # 实例化会话对象 会话对象让你能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持 cookie
        self.session = requests.Session()


# 生产者模式，用于封装获取想要下载内容的url
class Producer(AutoHomeThread):
    def run(self):
        while True:
            # 判断队列是否为空
            if self.page_queue.empty():
                break
            # 出队列，得到url
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        print('url:', url)
        # 发出请求
        response = self.session.get(url, headers=self.headers)
        text = response.text
        # 解析页面
        html = etree.HTML(text)
        links = html.xpath("//div[@class='uibox']//li//img/@src")
        for link in links:
            img_name = link.split('__')[-1]
            # 拼接图片下载地址，并将图片转换为高清图，替换掉图片清晰度
            img_url = "https:" + link.replace("t_autohomecar", "1024x0_1_q87_autohomecar")
            # 出队列得到(img_url, img_name)，给到self.detail_queue
            self.detail_queue.put((img_url, img_name))
            time.sleep(2)


# 消费者模式，用于封装下载想要下载的内容
class Consumer(AutoHomeThread):
    def run(self):
        while True:
            # 出队列得到上面出来的(img_url, img_name)
            img = self.detail_queue.get(timeout=60)
            self.download_image(img)

    # 封装一个下载函数，并存入文件
    def download_image(self, img):
        img_url, img_name = img
        if not os.path.exists('./汽车之家'):
            os.mkdir('./汽车之家')
        request.urlretrieve(img_url, os.path.join('./汽车之家/', img_name))
        print(img_name + ' 下载完成！')


# 主函数调用
def main():
    page_queue = Queue(20)
    detail_queue = Queue(500)
    urls = [
        'https://car.autohome.com.cn/pic/series/65-1.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-10.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-3.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-12.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-13.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-51.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-14.html#pvareaid=2042222'
    ]
    for url in urls:
        # 出队列
        page_queue.put(url)

    for x in range(1):
        # 调用生产者
        t = Producer(page_queue, detail_queue)
        # 线程调用
        t.start()

    for x in range(1):
        # 调用消费者
        t = Consumer(page_queue, detail_queue)
        t.start()


if __name__ == '__main__':
    main()
