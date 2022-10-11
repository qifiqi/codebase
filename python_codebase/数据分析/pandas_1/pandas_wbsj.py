import pandas as pd
import numpy as np
import re

aa = pd.read_csv('./sj/aa.csv')
# aa = pd.read_excel('./sj/aa.xlsx')

# aa = pd.DataFrame(np.arange(12).reshape((3,4)))
# a = {'aa': ['aa{}'.format(i) for i in range(20)],
#      'bb': ['bb{}'.format(i) for i in range(20)]}
# aa = pd.DataFrame(a)

# print(aa.head())
# print(aa.tail())

# print(aa.info())
a1 = []
aa = aa['人次']
for i in aa:
    one = re.findall('(.*?)万', i)[0]
    one = one.split('.')[0]
    a1.append(int(one))

t1 = pd.DataFrame(a1, columns=['aa'])
# print(t1[t1['aa'] > 100])

print(t1[(t1['aa'] > 3000) & (t1['aa'] < 8000)])
