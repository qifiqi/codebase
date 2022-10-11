from faker import Faker

fa = Faker("zh_CN")

print("随机职位：%s" % fa.job())  # 随机职位
print("女性名：%s" % fa.first_name_female())  # 女性名
print("男性名：%s" % fa.first_name_male())  # 男性名
print("随机生成全名：%s" % fa.name())  # 随机生成全名
print("男性全名：%s" % fa.name_female())  # 男性全名
print("女性全名：%s" % fa.name_male())  # 女性全名
print("生产国家：%s" % fa.country())
print("随机生成请求头: %s" % fa.chrome())
print("# 1~9的随机数 ：%s" % fa.random_digit_not_null())  # 1~9的随机数
