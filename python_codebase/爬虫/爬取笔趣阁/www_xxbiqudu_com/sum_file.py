# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/1622:03
# @Author  : 小符玩代码
# @Email   : 2737454073@qq.com
# @File    : kaoshibao.py
# @Software: PyCharm
import os
from tqdm import tqdm


def sum_file(path):
    list_dirs = os.listdir(path)
    if path[-1] == '/' or path[-1] == '\\':
        path = path[:-1]
    # 获取文件名
    file_title = os.path.split(path)[0]
    file_title = os.path.split(file_title)[-1]

    list_dirs = sorted(list_dirs, key=lambda x: int(x.split('-')[0]))
    ff = open(f'./{file_title}/{file_title}.txt', 'a+', encoding='utf-8')
    for file in tqdm(list_dirs):
        file_path = os.path.join(path, file)

        f = open(file_path, 'r', encoding='utf-8')
        title = file.split('-')[1].split('.')[0].strip() + '\n'
        ff.write(title)
        ff.write(f.read() + '\n')
        f.close()
    else:
        ff.close()


if __name__ == '__main__':
    sum_file('D:\专业\codebase\python_codebase\爬虫\爬取笔趣阁\剑来\章节')
