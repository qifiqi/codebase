"""一个打包的模块"""

# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/13 11:12
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : bale.py
# @Software: PyCharm
import os
import shutil
import sys
import time


def path_remove(path):
    """递归删除所有文件和文件夹--指定目录"""
    for i in os.listdir(path):
        path_b = os.path.join(path, i)
        if os.path.isdir(path_b):
            path_remove(path_b)
        else:
            os.remove(path_b)
    else:
        os.removedirs(path)


def bale_dir(path: str, packaging_type: str, owner: str = os.path.basename(__file__).split('.')[0],
             file_name: str = ''):
    start = time.time()
    dirs_name = path.split('\\')[-1]
    root_dir = f'{dirs_name}_打包'
    # 判断path是不是存在：
    if not os.path.exists(path):
        sys.stdout.write('path：路径不存在')
        return None

    # 在当前目录创建一个文件夹
    if os.path.exists(os.getcwd() + root_dir):
        path_remove(os.getcwd() + root_dir)
    else:
        os.mkdir(root_dir)

    # 判断packaging_type的类型是不是需要的类型
    if packaging_type not in ["zip", "tar", "gztar", "bztar", "xztar"]:
        sys.stdout.write('packaging_type：传入的参数压缩方式有问题')
        return None
    # 获取当前文件夹下的所有文件夹
    list_dir = [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))]
    # 打包每个文件夹
    for dir_name in list_dir:
        shutil.make_archive(
            base_name=f'{root_dir}/{dir_name}{file_name}',
            format=packaging_type,
            root_dir=os.path.join(path, dir_name),
            owner=owner,
        )
    stop = time.time()
    return f'{stop - start},{os.getcwd() + root_dir}'


if __name__ == '__main__':
    path = input("输入路径")
    packaging_type = input('输入压缩方式')
    owner = input('请输入写入用户')
    file_name = input('是否要加文件后缀，默认源文件名')
    print(bale_dir(path, packaging_type, owner, file_name))
