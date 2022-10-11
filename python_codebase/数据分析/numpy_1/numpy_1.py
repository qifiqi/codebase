import numpy as np

'''
t1 = np.array([1,2,3])
print(t1)
print(type(t1))
'''
# t1 = t2.shape
# print(t1)

# 数组形状
t1 = np.array(range(24))
print(t1)
print(t1.shape)
print('*' * 20)
t2 = t1.reshape((3, 8))
print(t2)
print(t2.shape)
print('*' * 20)
t3 = t1.reshape((2, 3, 4))
print(t3)
print(t3.shape)
# t1 = np.arange(24)
# print(t1/0)
