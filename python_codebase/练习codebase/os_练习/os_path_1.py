import os

file_path_txt = open('file_path.txt', 'a+', encoding='utf-8')

for root, dirs, files in os.walk(top='D:/比赛/练习/os_lj/aaaa'):
    print(root + '_' * 10)
    for file in files:
        # print(file)
        file_suffix = os.path.splitext(file)[1]
        file_path = os.path.join(root, file)
        # file_abs_path = os.path.abspath(file)
        # file_parent = os.path.dirname(file_path)
        # print(file_parent)
        # print(file_path)
        # print(file_abs_path)
        # print('*' * 70)
        if file_suffix == '.txt':
            file_path_txt.write(file_path)
            file_path_txt.write('\n')
            continue
        elif file_suffix == '.word':
            file_path_txt.write(file_path)
            file_path_txt.write('\n')
            continue
        elif file_suffix == '.zip':
            file_path_txt.write(file_path)
            file_path_txt.write('\n')
            continue
else:
    print('结束')
    file_path_txt.close()
