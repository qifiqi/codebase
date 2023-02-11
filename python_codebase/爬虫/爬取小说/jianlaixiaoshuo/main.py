import hashlib
import os
import time

from aligo import Aligo
import requests
from concurrent.futures import ThreadPoolExecutor
import queue
from tqdm import tqdm
from lxml import etree

"""
http://www.jianlaixiaoshuo.com/
"""

q = queue.Queue()
th = ThreadPoolExecutor(max_workers=32)

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33",
    "Referer": "https://www.tyxsw.org/read/38590/"
}

titles = "剑来"
titles_text = '正文'


def put_list(url: str):
    head['Referer'] = url
    response = requests.get(url=url, headers=head)
    html = etree.HTML(response.content.decode("utf-8"))

    global titles
    global titles_text
    titles_sum = html.xpath("/html/body/div[1]/div/dl/dt[1]/text()")[0]
    titles_text = html.xpath("/html/body/div[1]/div/dl/dt[2]/text()")[0]
    titles = html.xpath("/html/body/div[1]/div/div/div/h1/a/text()")[0]

    if not os.path.exists(f'./{titles}'):
        os.makedirs(f"./{titles}/{titles_sum}/")
        os.makedirs(f"./{titles}/{titles_text}/")

    dd_list = html.xpath("//dl/dd")

    for dd in dd_list[0:48]:
        path = "http://www.jianlaixiaoshuo.com" + dd.xpath('./a/@href')[0]
        get_text(None, path, titles_sum)

    for i, dd in enumerate(dd_list[48:]):
        path = "http://www.jianlaixiaoshuo.com" + dd.xpath('./a/@href')[0]
        q.put((i, path, titles_text))

    pass


def get_text(i, path, section):
    response = requests.get(url=path, headers=head)
    html = etree.HTML(response.content.decode("utf-8"))
    title = html.xpath('//*[@id="BookCon"]/h1/text()')[0]
    text_list = html.xpath('//div[@id="BookText"]//text()')
    print(f"{title} 写入文件")
    if i is not None:
        with open(f'./{titles}/{section}/{i}_{title}.txt', 'w+', encoding='utf-8') as files:
            files.write(title+"\n")
            for text in text_list[1:-1]:
                files.write(text.replace("$nbsp;", ''))
            files.write("\n")
    else:
        with open(f'./{titles}/{section}/{title}.txt', 'w+', encoding='utf-8') as files:
            files.write(title+"\n")
            for text in text_list[1:-1]:
                files.write(text.replace("$nbsp;", ''))
            files.write("\n")
    print(f"{title} 写入完成")


def sum_text():
    print(f'./{titles}/合并中')
    dirs_title = os.listdir(f'./{titles}/{titles_text}')
    dirs_title = sorted(dirs_title, key=lambda x: int(x.split('_')[0]))
    file = open(f'./{titles}/{titles}.txt', 'w+', encoding="utf-8")
    for dir in tqdm(dirs_title):
        with open(f'./{titles}/{titles_text}/{dir}', 'r', encoding='utf-8') as ff:
            file.write(ff.read().strip()+"\n\n")
            ff.close()
    file.close()


def main(url):
    put_list(url)
    print(q.qsize())

    while q.qsize() > 0:
        i, path, title_text = q.get()
        th.submit(get_text, i, path, title_text)

    time.sleep(32)


def get_ali():
    ali = Aligo()
    ali.move_file_to_trash(ali.get_file_list("62d80bbe9100e320545e48e0a7d918cf802e57f8")[-1].file_id)
    ali.sync_folder(
        local_folder=f"./{titles}",
        remote_folder="62d80bbe9100e320545e48e0a7d918cf802e57f8",
    )


def run():
    url_path = "http://www.jianlaixiaoshuo.com/"
    main(url_path)
    th.shutdown(wait=True)
    sum_text()
    get_ali()


if __name__ == '__main__':
    # run()
    get_ali()
    # sum_text()



