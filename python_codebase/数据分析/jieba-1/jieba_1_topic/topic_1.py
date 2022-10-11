import jieba

file = open('../jieba_测试_1.txt', 'r', encoding='utf-8')
# print(file.readlines())

count = {}

for i in file:
    aa = jieba.cut(i, cut_all=True)
    print('//'.join(aa))
    # for text in aa:
    #     if len(text) > 1:
    #         count[text] = count.get(text, 0) + 1
    print('**'*88)

    aa = jieba.cut(i, cut_all=False)
    print('/'.join(aa))

    print('**'*88)
    aa = jieba.cut_for_search(i)
    print('*'.join(aa))

