import random
from matplotlib import pyplot as pl
import matplotlib

'''
# 要注意顺序
x = range(2, 25, 2)

y = [12, 3, 234, 123, 541, 345, 34, 31, 23, 4, 12, 12]
# 设置图片大小，要注意要在绘图之前去设置
fig = pl.figure(figsize=(12, 8), dpi=80)

# 绘图
pl.plot(x, y)

# 设置x轴的刻度
pl.xticks(range(2, 25, 1))

# 设置y轴的刻度

# 保存图片
# pl.savefig('./i.png')  # pl.savefig('url地址')

# 显示图片
pl.show()
'''
from matplotlib import font_manager

'''
font = {'family': 'MicroSoft Vahei',
        'weight': 'bold',
        'size': 'larger'}
matplotlib.rc('font', **font)  # pass in the font dict as kwargs
'''
# 实例化font_manager

my_font = font_manager.FontProperties(fname='./ziti/Dengb.ttf', size=12)
y = [random.randint(20, 35) for i in range(120)]

x = range(120)

fig = pl.figure(figsize=(20, 8), dpi=80)

pl.plot(x, y)
x1 = [i for i in range(121)]
x2 = ["10时:{}分".format(i) for i in range(60)]
x2 += ["11时:{}分".format(i) for i in range(61)]

pl.xticks(x1[::4], x2[::4], rotation=45, fontproperties=my_font)

y1 = range(15, 40)
pl.yticks(y1)

pl.xlabel('时间', fontproperties=my_font)
pl.ylabel('温度', fontproperties=my_font)
pl.title('这个时两个小时的温度情况', fontproperties=my_font)

pl.show()
