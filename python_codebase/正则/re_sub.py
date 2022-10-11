import re

s = 'girl fr    ien   d'

"""
每次正则匹配到空格的时候都会调用aaa方法
然后将匹配到的内容传进去到方法中然后再来
判断或者进行其他操作

"""


def aaa(aa):
    print(aa.group())  # 输出匹配的字符串
    if aa.group() == ' ':
        return ' '
    else:
        return ''


if __name__ == '__main__':
    print(re.sub(r' +', aaa, s))
    print(re.subn(r' +', aaa, s))
