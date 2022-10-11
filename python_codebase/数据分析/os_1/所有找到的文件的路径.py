# 第8题：编写Python代码，实现以下任务：
# 1、搜索给定该路径下（包括子文件夹内）所有的word、pdf、txt、excel格式文件，并建立一个文件（fileList.txt）
# 存放所有找到的文件的路径。
# 2、运行代码，输入查找目录“\\搜索目录\\”
# 3、把运行结果文件保存到本地磁盘“\\home\\数据处理结果\\fileList.txt”中。
import os

file_list = []


def search_dir(start_dir):
    os.chdir(start_dir)
    list_dirs_file = []
    for dirs_all in os.walk(os.path.abspath(os.curdir)):
        for dirs in dirs_all[-1]:
            if dirs.split(".")[-1] in ["docx", "doc", "pdf", "xls", "xlsx", "txt"]:
                list_dirs_file.append(os.path.join(dirs_all[0], dirs))
    return list_dirs_file


start_dir = input("输入查找目录:")
file_list = search_dir(start_dir)
file = os.open("home\\数据处理结果\\fileList.txt",
               os.O_RDWR | os.O_CREAT | os.O_APPEND)
for dirs in file_list:
    os.write(file,(dirs+os.linesep).encode())
os.close(file)
# F:\\安院\\学习\\Python\\阶段性考试\\数据分析1\\搜索目录