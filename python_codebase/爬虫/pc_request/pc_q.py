import requests
import pandas as pd
import time


def openimg(url, data_path):
    reposes = requests.get(url)
    with open(f'./img/{data_path}', "wb") as a:
        a.write(reposes.content)
    a.close()


if __name__ == '__main__':
    i = 0
    img_path = pd.read_csv('D:/比赛/project_python/fxi/爬虫爬到的数据/img_清洗过.csv')
    img_path.set_index('Unnamed: 0', drop=True, inplace=True)
    for img in img_path.values:
        print(f'休息一秒钟,下载到{img[0]},\n以及下载到第{i + 1}张图片')
        i += 1
        time.sleep(1)
        data_path = f'{time.time_ns()}.jpg'
        print(data_path)
        openimg(img[0], data_path)
