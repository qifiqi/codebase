import re

aa = ['官网商城',
      '官方商城',
      '官网商城'
      ]
for i in range(len(aa)):
    aa[i] = re.sub(r'官网\S+', '官方', aa[i])
print(aa)
