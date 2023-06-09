from matplotlib import pyplot as plt
import numpy as np
import random
import pandas as pd

aa = np.array([random.randint(1, 100) for i in range(100)]).reshape(10, 10)

print(aa)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

fig = plt.figure(figsize=(12, 8), dpi=80)
sub = fig.add_subplot(1, 1, 1)

im = plt.imshow(aa, label='热力图')

plt.xticks([i for i in range(10)], [i for i in range(10)])
plt.yticks([i for i in range(10)], [i for i in range(10)])

plt.title('热力图')

cb = fig.colorbar(im, extend='both')  # 设置颜色柱
plt.grid()

plt.show()
