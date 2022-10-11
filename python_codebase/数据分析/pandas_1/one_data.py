import numpy as np
import pandas as pd
import re

data_path = './sj/examine_data.csv'
list = []
examin_Data = pd.read_csv(data_path, delimiter=',')
for i in examin_Data['性别']:
    i = re.sub('性', '', i)
    list.append(i)
examin_Data['性别'] = list
# t1 = examin_Data.groupby(by=['性别', '学历'])
# t1 = examin_Data['用户id'].groupby(by=[examin_Data['性别'], examin_Data['学历']]).count()

# for i, j in t1:
#     print(i)  # 分组名
#     print('-' * 100)
#     print(j)  # 数据
#     print('*' * 100)
t1 = examin_Data[['用户id']].groupby(by=[examin_Data['性别'], examin_Data['学历']]).count()
# t2 = examin_Data.groupby(by=[examin_Data['性别'], examin_Data['学历']])[['用户id']].count()
# t3 = examin_Data.groupby(by=[examin_Data['性别'], examin_Data['学历']]).count()[['用户id']]
# print(type(t1))
# 索引的方法
# print(t1)
print(t1.loc['女'].loc['初中及以下'])
