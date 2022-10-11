import pprint

import pandas
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['font.size'] = 20
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

data = pandas.read_csv('./xiaoshuo.csv')
data_lx = data['lx']
data_group = data_lx.groupby(by=data_lx.values).count()
data_group.drop('lx', inplace=True)

x = [i for i in range(1, len(data_group.index) + 1)]
y = [int(i) for i in data_group.values]

fig = plt.figure(figsize=(12, 8), dpi=80)

bar_t = plt.bar(x, [int(i) for i in data_group.values], width=0.5, label='类型分析')

plt.title('类型分析')

plt.xticks(x, [i for i in data_group.index])

for x, y in zip(x, data_group):
    plt.text(x, y,y,color='red')

plt.legend()

plt.savefig('./aa.jpg')


plt.show()
