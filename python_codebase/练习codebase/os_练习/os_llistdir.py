import os

'''
aa = os.listdir('D:/比赛')
for i in aa:
    aaa = os.listdir(f'D:/比赛/{i}')
    print(aaa)
'''
'''
dir_list = os.listdir('D:/比赛')
print(dir_list)
for cur_file in dir_list:
    # 获取文件的绝对路径
    path = os.path.join('D:/比赛/', cur_file)
    if os.path.isfile(path):  # 判断是否是文件还是目录需要用绝对路径
        print("{0} : is file!".format(cur_file))
    if os.path.isdir(path):
        print("{0} : is dir!".format(cur_file))
'''
#
# for root, dirs, files in os.walk(top='D:/比赛'):
#     # print(root)
#     # # print('-'*88)
#     # print(dirs)
#     # # print('_'*88)
#     print(files[0])
#     # print('+'*88)
#     if os.path.isfile(files[0]):
#         print(os.path.dirname(files[0]))
# '\n\n<><><><><> work dir <><><><><>'
for root, dirs, files in os.walk(top='D:/比赛/练习/os_lj/aaaa'):
    print
    '\n========================================'
    print("root : {0}".format(root))

    print("dirs : {0}".format(dirs))

    print("files : {0}".format(files))

    for file in files:
        try:
            print('-----------------------------------')

            # 文件名称
            file_name = os.path.splitext(file)[0]
            # 文件后缀
            file_suffix = os.path.splitext(file)[1]
            # 文件路径
            file_path = os.path.join(root, file)
            # 文件绝对路径
            file_abs_path = os.path.abspath(file)
            # 文件父路径
            file_parent = os.path.dirname(file_path)
            # 文件
            print("file : {0}".format(file))

            # 文件名称
            print("file_name : {0}".format(file_name))

            # 文件后缀
            print("file_suffix : {0}".format(file_suffix))

            # 文件路径
            print("file_path : {0}".format(file_path))

            # 文件绝对路径
            print("file_abs_path : {0}".format(file_abs_path))

            # 文件父路径
            print("file_parent : {0}".format(file_parent))

        except Exception as e:
            print("Exception", e)

