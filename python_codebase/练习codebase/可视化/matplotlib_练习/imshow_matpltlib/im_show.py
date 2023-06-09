import pandas as pd
import numpy as np
import datetime, sys
import matplotlib.pyplot as plt

LA_t2021 = pd.read_csv('LA_temperature_2010_hourly.csv')
# print(LA_t2021.head().to_string())
date = LA_t2021['DATE']
tmp = LA_t2021['HLY-TEMP-NORMAL']

nrec = len(LA_t2021)

temp_2d = np.zeros([24, 365])
for i in range(nrec):
    dt = datetime.datetime.strptime(
        '2010' + date[i],
        '%Y%m-%dT%H:%M:%S'
    )
    st = dt.timetuple()

    doy = st.tm_yday - 1  # 当前年份
    # print(doy)
    hr = st.tm_hour  # 一天中有几个小时
    # print(hr)
    temp_2d[hr, doy] = tmp[i]

temp_2d[0, 0] = temp_2d[23, 0]

# fig = plt.figure(figsize=(12, 8), dpi=80)  # 设置图片生成一个画图的白板
# sub = fig.add_subplot(111)  # 这个是将图片分块，如果是321这表示，将白板分成六块，3行2列的六块，其中最还一个一指的是第一块
# im = sub.imshow(temp_2d,
#                 aspect='auto',  # aspect='auto'|'equal' x/y轴等比例或者拉伸
#                 cmap='jet', vmin=5, vmax=temp_2d.max(),
#                 # cmap='jet',设置颜色表为jet vmin=5设置颜色范围的最小值, vmax=temp_2d.max()这个是最大值,
#                 # 这个是设置指定颜色表及其范围，

# )
# cb = fig.colorbar(im, extend='both')#设置颜色柱
# plt.show()

moth_arr = np.zeros(365, dtype=int)
dt0 = datetime.date(2010, 1, 1)
for i in range(365):
    dt = dt0 + datetime.timedelta(days=i)
    moth_arr[i] = dt.month
temp_2d_dinned = np.zeros([12, 12])
for imonth in range(1, 13):
    idx = np.where(moth_arr == imonth)[0]
    for ihr in range(12):
        temp_2d_dinned[ihr, imonth - 1] = \
            np.average(temp_2d[ihr * 2:(ihr + 1) * 2, idx])
fig = plt.figure(figsize=(12, 8), dpi=80)
sub = fig.add_subplot(111)
im = sub.imshow(temp_2d_dinned, aspect='auto',
                cmap='jet', vmin=10, vmax=25,
                origin='lower',
                extent=(0.5, 12.5, 0, 24)  # (xmin,xmax,ymin,ymax)
                )
cb = fig.colorbar(im, extend='both',
                  ticks=np.arange(10, 25.1, 3))
cb.ax.set_title(r'T/${}^{o}C$')

for imonth in range(1, 13):
    for ihour in range(1, 24, 2):
        t_text = int(temp_2d_dinned[int((ihour - 1) / 2), imonth - 1])
        if t_text > 20 or t_text < 13:
            c_text = 'w'
        else:
            c_text = 'k'
        sub.text(imonth, ihour,
                 '{:d}'.format(t_text),
                 ha='center', va='center',
                 color=c_text)

sub.set_xticks(np.arange(1, 13))
sub.set_yticks(np.arange(0, 25, 6))
sub.set_yticks(np.arange(0, 25), minor=True)
sub.set_xlabel(r'Month', fontsize=14)
sub.set_ylabel(r'Hour', fontsize=1)
fig.tight_layout()

plt.savefig('./imshow.jpg')

plt.show()
