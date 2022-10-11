import numpy as np
aa = np.loadtxt('./sj/aa.csv', encoding='utf-8', delimiter=',', dtype=object)

# t0 = np.zeros((aa.shape[0],1))
# t0 = np.ones((aa.shape[0],1))
# t0 = np.eye(10)
t0 = np.arange(100).reshape((4,25))
print(np.sum(t0,axis=1))
print(t0)