import os

data = [
    '符青',
    '陈宇轩',
    '向燕飞',
    '贺云鹏',
    '刘珂',
    '谢宇轩',
    '叶朝明',
    '杨明轩',
    '苏勇',
    '刘薇',
    '梁业成',
    '肖梅梅',
    '欧新宇',
    '彭威扬',
    '向长健',
    '黄俊杰',
    '蒋顺旗',
    '胡毅荣',
    '石永志',
    '周宇',
    '杨淑英',
    '易芸',
    '戴浪',
    '熊嘉成',
    '刘文广',
    '周智华',
    '蒋力',
    '李逸民',
    '熊辉',
    '吴江枫',
    '张鑫',
    '钟翾',
    '刘广平',
    '黄冀',
    '周阳轩',
    '钟长滚',
]


def panduan(file_name):
    """
    用来判断交了没有
    @param file_name: 传入的文件名
    """
    for i in data:
        if i in file_name:
            data.remove(i)


if __name__ == '__main__':
    for root, dirs, files in os.walk('提交文件夹/'):
        for file in files:
            panduan(file)

    aa = open('./结------------------------果.txt', 'w', encoding='utf-8')
    for i in data:
        aa.write(i+'\n')
    aa.close()
