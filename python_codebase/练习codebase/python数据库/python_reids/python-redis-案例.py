# 字典hash的使用
import redis

# 1 链接
red = redis.Redis(
    host="192.168.110.141",
    port=6379,
    password="123qweasd",
    decode_responses=True,  # 改成字符串简单来说就是设置中文显示
)

print(red.select(1))  # 切换到1号数据库

# 遍历keys
print("清空当前数据库")
for key in red.keys():  # 遍历所有
    # 删除
    red.delete(key)

# 添加map数据
print("添加map数据")
for i in range(10):
    red.hset("one", str(i), f"---------{i}--------")

# 查看所有
print("查看所有")
for num1, num2 in red.hgetall("one").items():
    print(num1, num2)

print("查看一个数据")
print(red.hget("one","1"))

red.close()
