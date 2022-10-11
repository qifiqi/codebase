import numpy as np
from matplotlib import pyplot as pl
import pandas as pd
from matplotlib import font_manager as font

examine = pd.read_csv('../pandas_1/sj/examine_qxifuo.csv', delimiter=',', skiprows=0)
# print(examine.columns)

my_font = font.FontProperties(fname='./方正粗黑宋简体.ttf', size=16, family='sans-serif')
pl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
pl.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置

cishu = []
xiazaiqvdas = []
xiazai = examine.drop_duplicates('下载渠道')
for xiazaiqvda in xiazai['下载渠道']:
    rshu = len(examine[examine['下载渠道'] == xiazaiqvda])
    cishu.append(rshu)
    xiazaiqvdas.append(xiazaiqvda)
print(cishu)
print(xiazaiqvdas)
fig = pl.figure(figsize=(14, 8), dpi=80)
sub = fig.add_subplot(111)


# autopct自定义函数来设置
def fount(pct):
    return '{:.1f}'.format(pct)


wedges, texts, autottexts = sub.pie(cishu, labels=xiazaiqvdas,
                                    explode=[0.01, 0.01, 0.01, 0.01, 0.01, 0.06, 0.01, 0.01],
                                    autopct='%.1f%%',
                                    textprops=dict(fontsize=16),  # 设置字体信息要传入字典
                                    radius=0.9,  # 设置饼的半径
                                    shadow=True,  # 设置阴影
                                    wedgeprops=dict(
                                        edgecolor='k',  # s设置饼的边框为黑色
                                        width=0.8  # 设置饼的宽带
                                    ),  # 接受一个字典用来设置饼的属性
                                    )
for i in range(len(texts)):
    texts[i].set_color('k')  # 设置颜色
    texts[i].set_size(20)  # 设置大小
    texts[i].set_weight('bold')  # 设置字符粗细
# bbox_to_anchor=(-0.14, -0.11, 0.5, 0.5)自定义位置
pl.legend(loc=4, bbox_to_anchor=(-0.14, -0.12, 0.30, 0.35), prop=my_font)

pl.title('下载渠道', fontproperties=my_font)

fig.tight_layout()
pl.show()
