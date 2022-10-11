import random
from matplotlib import pyplot as pl
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='./ziti/Dengb.ttf', size=12)
# 这个是x轴以及设置的x轴数据
x = [i for i in range(11, 31)]
x_s = ['{}岁'.format(i) for i in range(11, 31)]

y_1 = [random.randint(0, 6) for i in range(11, 31)]
y_2 = [random.randint(0, 6) for i in range(11, 31)]

# 设置图片大小
pl.figure(figsize=(12, 8), dpi=80)

# 绘图两次
pl.plot(x, y_1, label='自己')
pl.plot(x, y_2, label='同桌')

# 设置x轴
pl.xticks(x, x_s, rotation=45, fontproperties=my_font)

# 设置x轴y轴以及标题的内容
pl.xlabel('岁数', fontproperties=my_font)
pl.ylabel('个数', fontproperties=my_font)
pl.title('男朋友的人数走势', fontproperties=my_font)

# 绘制网格
pl.grid(alpha=0.4)

# 添加图列
pl.legend(prop=my_font)

# 显示图片
pl.show()
