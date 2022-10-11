import os
import shutil

"""
print(os.getcwd())
# 更改当前目录
print(os.chdir(r'D:\专业\python数据\os_lx\aaaa\asdf'))
print(os.getcwd())
"""
# 创建空目录
# os.mkdir(path=r"D:\专业\python数据\os_练习\aaaa\aaa")
# 多级目录
# os.makedirs(r"D:\专业\python数据\os_练习\aaaa\aa\a\a\a\\a\a")
# 删除空目录
# os.rmdir(path=r"D:\专业\python数据\os_练习\aaaa\aaa")
# 删除不为空的目录
# shutil.rmtree(r'D:\专业\python数据\os_练习\aaaa\新建文件夹')
# 重命名
os.rename(src=r'/os_练习\aaaa\nnnnnn', dst=r'/os_练习\aaaa\nnnn')  # 只修改一个
os.renames(old=r'D:\专业\python数据\os_lx\aaaa\nnnn', new=r'D:\专业\python数据\os_lx\aaaa\n')  # 只修改多个

