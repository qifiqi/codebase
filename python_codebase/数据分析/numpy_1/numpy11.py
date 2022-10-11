import numpy as np

t1 = np.arange(12).reshape(2, 6)
# t2 = np.arange(12,24).reshape(2,6)
print(t1)
# t1[[0, 1], :] = t1[[1, 0], :]
t1[:,[2,4]]=t1[:,[4,2]]
print(t1)
# print(t2)
#
# print(np.hstack((t1,t2)))
