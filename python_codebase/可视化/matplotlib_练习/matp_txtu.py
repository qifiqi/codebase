import random

from matplotlib import pyplot as pl

from matplotlib import font_manager as font

my_font = font.FontProperties(fname='./ziti/Dengb.ttf', size=12)
b = [17, 28, 24, 32, 37, 37, 19, 18, 22, 29, 20, 15, 24, 17, 27]
c = [22, 18, 31, 27, 17, 33, 24, 16, 23, 26, 39, 22, 32, 28, 22]
a = ['C39512', 'C29825', 'C47139', 'C37948', 'H23580', 'H43359',
     'H40194', 'H37906', 'H41039', 'H40991', 'H33587', 'H40729',
     'H39047', 'H48300', 'H29829']

pl.figure(figsize=(12, 8), dpi=80)
b_1 = list(range(len(a)))
c_1 = [i+0.2 for i in b_1] 

pl.bar(b_1, b, width=0.2,label='上帝覅')
pl.bar(c_1, c, width=0.2,label='上帝')

pl.legend(prop=my_font)

pl.grid(alpha=0.3)
pl.xticks(range(15), a, fontproperties=my_font)

pl.show()
