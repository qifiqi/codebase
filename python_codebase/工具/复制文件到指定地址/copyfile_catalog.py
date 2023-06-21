# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/5/1422:42
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : copyfile_catalog.py
__author__ = 'Small Fu'

"""
1.复制文件或文件夹下的子文件到指定地址
2.多线程复制
3.可以指定或者不指定选择文件类型：如
    mp3,mp4,jpg,png等

"""

import os
import time

from concurrent.futures import ThreadPoolExecutor

file_set = set()

file_type = None

sourceFile = ""
targetFile = "./" + time.time().__str__()
"""
    :param targetFile:目标文件夹
    :param sourceFile:源文件地址
"""


def get_file_all(sourceFile):
    """
    获取所有文件
    :param sourceFile: 初始目录地址
    :return:
    """
    if not os.path.exists(sourceFile):
        print("目录不存在,sourceFile:", sourceFile)
        return False

    list_dir = os.listdir(sourceFile)
    for f in list_dir:
        _route = os.path.join(sourceFile, f)
        if os.path.isfile(_route):
            file_set.add(_route)
        elif os.path.isdir(_route):
            get_file_all(_route)


def filterFiles():
    """
    选择需要的文件
    :param file_type:文件类型，mp3,mp4,jpg,png等，也可以传递一个列表   None为所有文件都要
    :return:
    """
    pass

    _file_set = list(file_set)
    file_set.clear()
    if file_type is None or len(file_type) < 1:
        return
    for f in _file_set:
        _type = os.path.splitext(f)[-1][1:]
        if _type not in file_type:
            continue
        file_set.add(f)


def copyingFiles(sourceFile):
    """
    复制文件到目标文件夹

    :return:
    """
    if not os.path.exists(sourceFile):
        print("目录不存在,sourceFile:", sourceFile)
        return False
    if not os.path.exists(targetFile):
        print("目录不存在,sourceFile:", targetFile)
        return False
    _file = os.path.split(sourceFile)[-1]
    _target = os.path.join(targetFile, _file)
    inputF = open(sourceFile, "rb")
    _size = (os.path.getsize(sourceFile) // 10) + 1024
    outputF = open(_target, "wb+")
    while True:
        _data = inputF.read(_size)
        if not _data:
            break
        outputF.write(_data)
    inputF.close()
    outputF.close()
    # _data = inputF.read()
    # inputF.close()
    # with open(_target, "wb+") as outputF:
    #     outputF.write(_data)
    print(_file)


def main():
    """
    主方法
    :return:
    """

    get_file_all(sourceFile)
    filterFiles()
    print(f"一共有{len(file_set)}个{'-'.join(file_type)}文件")
    with  ThreadPoolExecutor() as threads:
        threads.map(copyingFiles, file_set)


if __name__ == '__main__':
    file_type = [str.lower(i) for i in
                 input("输入需要的类型，可以数据多个用‘-’隔开 \n不输入为全部文件都需要\n").split('-')]
    sourceFile = input("输入源文件夹：")
    targetFile = input("输入输出文件夹可以不输入：")
    if len(targetFile) < 1:
        targetFile = "./" + time.time().__str__()
        os.makedirs(targetFile)
    main()
