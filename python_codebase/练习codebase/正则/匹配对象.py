import re

m = re.match(r'(http://www|WWW)\.(.*)\..{3}', 'http://www.python.org')
print('输出匹配到的字符串')
print(m.group())
print('匹配第一个圆括号中的内容')
print(m.group(1))
print('匹配第二个圆括号中的内容')
print(m.group(2))
print('输出第一组字符串的起始位置')
print(m.start(1))
print('输出第二组字符串的起始位置')
print(m.start(2))
print('输出字符串的结束位置')
print(m.end(0))
print('输出第一个的起始和结束位置')
print(m.span(1))

