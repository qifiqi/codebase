import numpy as np
from matplotlib import font_manager as font
from matplotlib import pyplot as pl
import pandas as pd
import re

examine = pd.read_csv('../pandas_1/sj/examine_qxifuo.csv', delimiter=',', skiprows=0)
my_font = font.FontProperties(fname='./方正粗黑宋简体.ttf', size=16, family='sans-serif')
# 拆分时间
nian = []
yue = []
for aa in examine['注册时间']:
    nians, yues, r = aa.split('-')
    nian.append(nians)
    yue.append(yues)
examine['年份'] = nian
examine['月份'] = yue
zorshu = {}
# print(examine['注册时间'])
# y轴
for nian in examine['年份'].drop_duplicates():
    lists = []
    aa = []
    bb = []
    cc = []
    for times in examine['注册时间']:
        aaa = re.findall('^' + nian + '-[1-4]{1}-\d{1,2}', times)
        if len(aaa) != 0:
            aa.append(aaa)
        else:
            continue

    for times in examine['注册时间']:
        bbb = re.findall('^' + nian + '-[5-8]{1}-\d{1,2}', times)
        if len(bbb) != 0:
            bb.append(bbb)
        else:
            continue
    for times in examine['注册时间']:
        ccc = re.findall('^' + nian + '-([9]|1[1-2]){1,2}-\d{1,2}', times)
        if len(ccc) != 0:
            cc.append(ccc)
        else:
            continue
    lists.append(len(aa))
    lists.append(len(bb))
    lists.append(len(cc))
    zorshu[nian] = lists
zorshu['2017'][0] = 100
zorshu['2019'][2] = 100
print(zorshu)
# x轴
nian_1x = [1, 1.5, 2]
nian_2x = [i + 0.1 for i in nian_1x]
nian_3x = [i + 0.1 for i in nian_2x]
# 设置图片大小
pl.figure(figsize=(14, 8), dpi=80)
# 绘图
pl.bar(nian_1x, zorshu['2017'], width=0.1, label='2017', color='#7B68EE')
pl.bar(nian_2x, zorshu['2018'], width=0.1, label='2018', color='#87CEEB')
pl.bar(nian_3x, zorshu['2019'], width=0.1, label='2019', color='#98FB98')
# 设置每个条形的标签
# 2017的数字标签
for a, b in zip(nian_1x, zorshu['2017']):
    pl.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=13)
# 2018的数字标签
for a, b in zip(nian_2x, zorshu['2018']):
    pl.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=13)
# 2019的数字标签
for a, b in zip(nian_3x, zorshu['2019']):
    pl.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=13)

# 设置x轴的刻度
pl.xticks(nian_2x, ['1-4月', '5-8月', '9-12月'], fontproperties=my_font)
# 设置上下限制
pl.ylim(0, 7000)
pl.xlim(0.75, 2.5)
# 标题，x和y轴标题
pl.title('进三年的人数情况', fontproperties=my_font)
pl.ylabel('注册人数', fontproperties=my_font, loc='top', rotation=0)
pl.xlabel('注册年份', fontproperties=my_font, loc='right')
# 图列
pl.legend(loc=2, prop=my_font)
# 显示网格
pl.grid(alpha=0.4)
# 显示图片
pl.show()
