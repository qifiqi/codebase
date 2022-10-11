import numpy as np
import pandas as pd
import re

'''
一 数据清洗与分析
1、	将用户信息表中用户id数据统一格式为：CXXXXX (以C开头)
2、	将用户信息表中注册时间数据统一格式为：yyyy-mm-dd (例如2019-4-10)
3、	处理其他异常数据，并进行重新存储。
4、	将用户信息表中所有省份空白项数据进行删除。
5、	分析出玩家数量（用户）排名前三的省份。
6、	分析用户各学历层次占比。
7、	分析用户最常用的支付手段

'''
# 读取数据
examine = pd.read_csv('../pandas_1/sj/examine_data.csv', delimiter=',', skiprows=0)
# 这个是看看是不是nan是的话就是true不是就是false
# print(pd.isnull(examine))
# 这个是看数组的列索引
# print(examine.columns)
# 这个是看数组中有没有nan有就返回多少个
# print(np.count_nonzero(examine != examine))
# print('%'*50)
# 根据列索引来取一列

# 1、	将用户信息表中用户id数据统一格式为：CXXXXX (以C开头)
userid = []
for uid in examine['用户id']:
    # r'\D'匹配全部的不为数字的字符全部替换为C
    uid = re.sub(r'\D', 'C', uid)
    userid.append(uid)
examine['用户id'] = userid

# 2、	将用户信息表中注册时间数据统一格式为：yyyy-mm-dd (例如2019-4-10)
user_dt = []
for dt in examine['注册时间']:
    # r'\D'匹配全部的不为数字的字符全部替换为C
    dt = re.sub(r'\D', '-', dt)
    user_dt.append(dt)
examine['注册时间'] = user_dt

# 3、	处理其他异常数据，并进行重新存储。
# 保存为csv格式
examine.to_csv('./examine_qxifuo.csv', index=0)

# 4、	将用户信息表中所有省份空白项数据进行删除。
# 这个是重新赋值，去除数组中为nan的值，按照行来算，只要有nan就删除
# inplace=True如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据
# 用了以后不可以在重新赋值到Dataframe中，因为加了参数以后直接改变了无需重新赋值
cccc = examine.dropna(axis=0, how='any', inplace=True)
print(cccc)
print(np.count_nonzero(examine['所属省份'] != examine['所属省份']))

# 5、	分析出玩家数量（用户）排名前三的省份。
sheng = []
for shengf in examine.drop_duplicates(subset='所属省份')['所属省份']:
    sum_ex = examine[examine['所属省份'] == shengf]
    lists = [shengf, len(sum_ex)]
    sheng.append(lists)
# print(shengf_s)
sheng = pd.DataFrame(sheng, columns=['省份', '人数'])
qsan = sheng.sort_values('人数', ascending=False).head(3)
print('*' * 50)
print('玩家数量（用户）排名前三的省份')
print(qsan)

# 6、	分析用户各学历层次占比。
# print(examine.columns)
education = []
xlis = examine.drop_duplicates(subset='学历')['学历']
for xli in xlis:
    sum_ex = examine[examine['学历'] == xli]
    lists = [xli, '%.5f%%' % (len(sum_ex) / len(examine)), len(sum_ex)]
    education.append(lists)
education = pd.DataFrame(education, columns=['学历', '占比', '人数'])
print('*' * 50)
print('用户各学历层次占比。')
print(education)

# 7、	分析用户最常用的支付手段
payment = pd.read_csv('../pandas_1/sj/用户流水.csv', delimiter=',', skiprows=0)
# print(payment.columns)
payment_way = []
zhifu = payment.drop_duplicates(subset='支付方式')['支付方式']
for fs in zhifu:
    sum_ex = payment[payment['支付方式'] == fs]
    lists = [fs, len(sum_ex)]
    payment_way.append(lists)
payment_way = pd.DataFrame(payment_way, columns=['支付方式', '人数'])
zuichangyong = payment_way.sort_values('人数', ascending=False).head(1)
print('*' * 50)
print('最常用的支付方式:')
print(zuichangyong)
