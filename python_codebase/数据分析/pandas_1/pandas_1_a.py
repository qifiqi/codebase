import pandas as pd

t1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
print(t1)
print(t1.index)
for i in t1.index:
    print(i)
print(t1.values)
