'''
利用string库和os库编写程序，去除开单日期中的‘.’、‘/’符号，月和日保持2位，不足需要补齐，最后输出日期yyyyMMdd(20211207)。
把处理后的结果保存到‘\\home\\数据处理结果\\kdDate.csv’中
'''
import csv
import datetime
import xlrd

wj_path = 'C:\\Users\\14404\\Desktop\\数据分析\\原始数据-某图书机构在各电商平台销售数据 1130.xls'
# 工作簿
file = xlrd.open_workbook(wj_path)
# 第一个工作表
gzb = file[0]
# 行数
hs = gzb.nrows
print(hs)
# 列数
ls = gzb.ncols
print(ls)

# 遍历所有行
for i in range(1, hs):
    lv = []
    dyg = gzb.cell(i, 3).value
    # print(dyg)
    # 判断是不是被转换为float类型
    if type(dyg) is float:
        # 拿取时间类型的数据
        dv = xlrd.xldate_as_tuple(dyg, file.datemode)
        # 转换为python的时间类型
        shi = datetime.date(dv[0], dv[1], dv[2])
    else:  # 没有被转换为float类型
        tp = tuple(str(dyg).split('.'))
        shi = datetime.date(int(tp[0]), int(tp[1]), int(tp[2]))
    jg = str(shi).replace('-', '')

    # 将excle的行转换成list
    # [0, 1, 2, 4, 5, 6, 7, 8, 9, 10]
    lv.append(gzb.cell(i, 0).value)
    lv.append(int(gzb.cell(i, 1).value))
    lv.append(gzb.cell(i, 2).value)
    lv.append(jg)
    for j in range(4, 7):
        value = gzb.cell(i, j).value
        lv.append(value)
    lv.append(int(gzb.cell(i, 7).value))
    lv.append(int(gzb.cell(i, 8).value))
    lv.append(gzb.cell(i, 9).value)
    lv.append(int(gzb.cell(i, 10).value))
    print(lv)
    # 保存到csv
    path = 'D:\\home\\数据处理结果\\kdDate.csv'
    # 打开要保存的文件
    xie = open(path, 'a', encoding='utf-8')
    # 创建写入对象
    obj = csv.writer(xie)
    # 写入数据
    obj.writerow(lv)
    # 关闭文件
    xie.close()
