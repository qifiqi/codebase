import requests, multiprocessing  # 多进程
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor  # 异步并发包

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    'Referer': 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4',
}




def get_html(url):
    # print('html当前进程为{}'.format(multiprocessing.current_process().pid))  # 打印当前进程的pid

    html = requests.get(url, headers=headers)
    threadpools = ThreadPoolExecutor(max_workers=3)  # 创建线程池3个线程
    print(html.status_code)
    soup = BeautifulSoup(html.text, 'lxml')
    urls = soup.select('.subject-item .info a')  # 获取 a 标签
    for url in urls:
        link = url['href']  # 获取书本链接
        threadpools.submit(get_link, link)  # 获取每本书都提交 1 个线程


def get_link(url):
    # print('获取书的父进程为{}'.format(multiprocessing.current_process().pid))  # 打印当前进程的pid

    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    title = soup.select_one('#wrapper h1 span').text  # 获取标题
    print(title)


if __name__ == '__main__':
    urls = ['https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4',
            'https://book.douban.com/tag/%E9%9A%8F%E7%AC%94',
            'https://book.douban.com/tag/%E6%96%87%E5%AD%A6', ]

    with ProcessPoolExecutor(max_workers=3) as p:  # 创建 3 个进程
        for url in urls:
            p.submit(get_html, url)  # 每个进程都提交给get_html

# 在分类不多的情况下 可以考虑 1 个分类 创建 1 个进程
# 假如处理大量任务  比如有 10000 个任务
# 则结合你服务器的当前状态 决定进程池和线程池大小
# 由于进程池和线程池  存在可复用性  可反复利用池的东西
# 正常情况下 三分之一即可 比如 100 个任务  池的大小为 30


# 注意：
# 网络爬虫 如果线程大于 3 就很容易造成封IP
# 要么线程开小点  爬慢点
# 要么构建IP代理池  定期更换IP  参考往期视频
