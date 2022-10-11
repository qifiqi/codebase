import numpy as np

t1 = np.loadtxt('./sj/aa.csv', encoding='utf-8', delimiter=',', dtype=str, skiprows=1, unpack=True)
t2 = np.loadtxt('./sj/aa.csv', encoding='utf-8', delimiter=',', dtype=str, skiprows=1)
print(t1)
print(t2)
print('&' * 100)
print(t1[[2, 3,1], [3, 2,2]])
