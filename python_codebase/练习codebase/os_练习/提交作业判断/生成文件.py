import pandas as pd
import os
data = pd.read_csv(r'C:\Users\FQCj\Desktop\aa.csv', names=['q'], encoding='gbk')['q']

os.mkdir(r'D:\专业\python数据\os_练习\作业')

for i in data:
    with open(rf'D:\专业\python数据\os_练习\作业\{i}.docx', 'a+', encoding='utf-8') as a:
        a.write(i)
        a.close()
