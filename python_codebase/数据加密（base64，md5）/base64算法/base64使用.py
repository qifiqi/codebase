import base64

data = b'data'
# 加密
data = base64.b64encode(data)
print(data)
data = base64.b64encode(data)
print(data)
# 解密
data = base64.b64decode(data)
print(data)
data = base64.b64decode(data)
print(data)
