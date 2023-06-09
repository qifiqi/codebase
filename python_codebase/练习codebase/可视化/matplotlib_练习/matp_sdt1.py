import random

from matplotlib import pyplot as pl

from matplotlib import font_manager as font

my_font = font.FontProperties(fname='./ziti/Dengb.ttf', size=12)

y_3 = [random.randint(10, 20) for i in range(10, 20)]
y_10 = [random.randint(10, 30) for i in range(20, 30)]

x = range(1, 11)
x_1 = range(32, 42)
fig = pl.figure(figsize=(12, 8), dpi=80)

pl.scatter(x, y_10, label='无语一号')
pl.scatter(x_1, y_3, label='无语二号')

# 添加图例
pl.legend(loc=1, prop=my_font)

# 总的x轴
x_zo = list(x) + list(x_1)

x_x = ['无语{}号'.format(i) for i in range(1, 11)]
x_1x = ['无语{}号'.format(i) for i in range(32, 42)]
# 总的x轴中文刻度
x_xzo = list(x_x) + list(x_1x)
pl.xticks(x_zo, x_xzo, fontproperties=my_font, rotation=45)

# 添加描述信息
pl.xlabel('无语', fontproperties=my_font)
pl.ylabel('无语程度', fontproperties=my_font)
pl.title('无语类比', fontproperties=my_font)

pl.show()
