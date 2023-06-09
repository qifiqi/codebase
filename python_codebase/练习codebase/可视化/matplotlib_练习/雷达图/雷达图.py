import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('../chn_province_new.csv')

data.sort_values('confirmedCount', ascending=True, inplace=True)
data.drop_duplicates('provinceName', keep='last', inplace=True)

data_h = data[data['provinceName'] == '湖北']


# x = [(i / 100) * np.pi for i in range(0, 115, 20)]
x = [(i / 100) * np.pi for i in range(0, 200, 34)]

y = [data_h['currentConfirmedCount'].values[0]/100,
     data_h['confirmedCount'].values[0]/10000,
     data_h['suspectedCount'].values[0]/10000,
     data_h['curedCount'].values[0]/10000,
     float(str(data_h['curedRate'].values[0]).replace('%', ''))/10,
     str(data_h['deadRate'].values[0]).replace('%', ''),
     ]
print(y)
fig = plt.figure()
# 设置为极坐标格式
ax = fig.add_subplot(111, polar=True)

plt.plot(x, y, 'o-', linewidth=2, label='红小豆行情雷达图')
plt.fill(x, y, 'r', alpha=0.5)

plt.ylim(0,5)

plt.show()
