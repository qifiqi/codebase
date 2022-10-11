import numpy as np
from matplotlib import pyplot as pl

aa = np.loadtxt('./sj/aa.csv', encoding='utf-8', delimiter=',', dtype=object, skiprows=1)

# 取出票价,并算出最大 和最小
fares = aa[1:, -1]
# 确定要分多少组
print(fares)
d = 3
bin_num = ((fares.max()) - fares.min()) // d
# # 绘图
# pl.figure(figsize=(20, 8), dpi=80)
#
# pl.hist(fares, bin_num)
#
# pl.show()
