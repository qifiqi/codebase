from wordcloud import WordCloud
import jieba
from tqdm import tqdm


def tingyci():
    tinyci = [line.strip() for line in open('停用词.txt', 'r', encoding='utf-8').readlines()]
    return tinyci


def jieba_fci(texts):
    tyc = tingyci()
    tyc = tyc + ['我们', '一个', '不知', '不能', '如此']
    list_data = []
    dict_data = {}
    for text in tqdm(texts):
        for a in jieba.cut_for_search(text):
            a = a.strip()
            if a not in tyc and len(a) > 1:
                list_data.append(a)
                dict_data[a] = dict_data.get(a, 0) + 1

    txt = ' '.join(list_data)
    wordcloud_ht_txt(txt)
    wordcloud_pci(dict_data)


def wordcloud_ht_txt(txt):
    wordclouds = WordCloud(
        font_path='/jieba-1/jieba_1_topic/STXINGKA.TTF',
        width=600,
        height=700,
        background_color='white',
    )
    wordclouds.generate(txt)
    wordclouds.to_file('./文本词云图.png')


def wordcloud_pci(dict_data):
    wordclouds = WordCloud(
        font_path='/jieba-1/jieba_1_topic/STXINGKA.TTF',
        width=600,
        height=700,
        background_color='white',
    )
    wordclouds.fit_words(dict_data)
    wordclouds.to_file('./这个是频次词云图.png')


if __name__ == '__main__':
    texts = open(r'D:\bs\2020python开发\djnago-爬虫\爬虫\urllib-bs4\三国演义\三国演义.txt', 'r', encoding='utf-8').readlines()
    jieba_fci(texts)
