
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

my_font = FontProperties(fname='./STSONG.TTF', size=14)
data_leidatu = pd.read_table('D:\\home\\商品报价统计.txt', delimiter=',')
data = data_leidatu.copy()
data_hxd = data[data['商品名称'] == '红小豆'].copy()

data_hxd['日期'] = data_hxd['时间'].apply(lambda x: str(x).split('/')[0])
data_hxd['报价'] = data_hxd['报价'].apply(lambda x: str(x).split('.')[0])
data_hxd['报价'] = data_hxd['报价'].astype('int64')
data_hxd_time2021 = data_hxd.groupby('日期')

hxd_sum = round((data_hxd_time2021['报价'].sum()) / 10000)['2021']
hxd_mean = round((data_hxd_time2021['报价'].mean()) / 100)['2021']
hxd_median = round((data_hxd_time2021['报价'].median()) / 100)['2021']
hxd_max = round((data_hxd_time2021['报价'].max()) / 100)['2021']
hxd_min = round((data_hxd_time2021['报价'].min()) / 100)['2021']
hxd_std = round((data_hxd_time2021['报价'].std()) / 100)['2021']



y = [hxd_sum, hxd_mean, hxd_median, hxd_max, hxd_min, hxd_std]

x = [(i / 100) * np.pi for i in range(0, 200, 34)]

feature = ['总和：单位*10000', '平均数：单位*100', "中位数：单位*100", "最大值：单位*100", "最小值：单位*100", "标准差：单位*100"]

# 绘图
fig = plt.figure()

# 设置为极坐标格式
ax = fig.add_subplot(111, polar=True)

plt.plot(x, y, 'o-', linewidth=2, label='红小豆行情雷达图')
plt.fill(x, y, 'r', alpha=0.5)

plt.xticks(x, feature, fontproperties=my_font)

plt.ylim(0, 400)

# plt.savefig('D:\\home\\数据分析与可视化结果\\红小豆行情雷达图.jpg')
#
plt.show()
