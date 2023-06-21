# coding=utf-8
import json

from ebooklib import epub


class book_epub:
    def __init__(self, title, author, briefIntroduction):
        self.briefIntroduction = briefIntroduction
        self.author = author
        self.title = title
        self.book = epub.EpubBook()
        self.book.set_identifier('sample123456')
        self.book.set_title(self.title)
        # self.book.set_language('ch')
        self.book.add_author(self.author)

        self.content_list = []

    def set_content(self, uid, title, file_name, content, css):
        con_item = epub.EpubHtml(title=title,
                                 file_name=file_name,
                                 uid=uid,
                                 content=content
                                 )
        con_item.set_content(content)
        self.content_list.append(
            con_item
        )
        for i in css:
            css = epub.EpubItem(uid=i, file_name=i, media_type="text/css", content=css[i])
            con_item.add_item(css)
        self.book.add_item(con_item)

    def save_img(self, uid, file_name, image_content):
        img_item = epub.EpubImage(uid=uid, file_name=file_name, media_type='image/jpg',
                                  content=image_content)
        self.book.add_item(img_item)

    def save_css(self, uid, file_name, content):
        nav_css = epub.EpubItem(uid=uid, file_name=file_name, media_type="text/css",
                                content=content)
        self.book.add_item(nav_css)

    def save(self):
        self.book.toc = (epub.Link('intro.xhtml', self.briefIntroduction, self.briefIntroduction),
                         (epub.Section('目录'),
                          (i for i in self.content_list))
                         )
        # add navigation files
        self.book.add_item(epub.EpubNcx())
        self.book.add_item(epub.EpubNav())

        # create spine
        self.book.spine = ['nav', *self.content_list]
        path = f'{self.title}.epub'
        print(path)
        # create epub file
        epub.write_epub(path, self.book, {})

import codecs
from html import escape
import os
import json

def txt_to_xhtml(txt_file, xhtml_file):
    with codecs.open(txt_file, 'r', 'utf-8') as f:
        lines = f.readlines()

    with codecs.open(xhtml_file, 'w', 'utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n')
        f.write('<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        f.write('<style>\np {font-family: Arial; font-size: 14px;}\n</style>\n</head>\n<body>\n')
        f.write('<h1>{}</h1>\n'.format(escape(lines[0])))
        for line in lines[1:]:
            f.write('<p>{}</p>\n'.format(escape(line)))
        f.write('</body>\n</html>')






def traverse_txt_files(dir,types):
    file_info_list = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(f".{types}"):
                number, _ = file.split("_")
                txt_to_xhtml(f"{root}/"+file,"./html/"+file.split(".")[0]+'.xhtml')
                file_info = {"parent_dir": root, "file_name": file.split(".")[0]+'.xhtml', "number": int(number)}
                file_info_list.append(file_info)

    file_info_list.sort(key=lambda x: x['number'])
    return json.dumps(file_info_list, ensure_ascii=False)





if __name__ == '__main__':
    book = book_epub('我在精神病院学斩神','你是否想过，在霓虹璀璨的都市之下，潜藏着来自古老神话的怪物？你是否想过，在那高悬于世人头顶的月亮之上，伫立着守望人间的神明？你是否想过，在人潮汹涌的现代城市之中，存在代替神明行走人间的超凡之人？人类统治的社会中，潜伏着无数诡异；在那些无人问津的生命禁区，居住着古老的神明。炽天使米迦勒，冥王哈迪斯，海神波塞冬……而属于大夏的神明，究竟去了何处？在这属于“人”的世界，“神秘”需要被肃清！','你是否想过，在霓虹璀璨的都市之下，潜藏着来自古老神话的怪物？你是否想过，在那高悬于世人头顶的月亮之上，伫立着守望人间的神明？你是否想过，在人潮汹涌的现代城市之中，存在代替神明行走人间的超凡之人？人类统治的社会中，潜伏着无数诡异；在那些无人问津的生命禁区，居住着古老的神明。炽天使米迦勒，冥王哈迪斯，海神波塞冬……而属于大夏的神明，究竟去了何处？在这属于“人”的世界，“神秘”需要被肃清！')
    # item = json.loads(open("./a.json", "rb").read())
    
    data = json.loads(traverse_txt_files("./text",'txt'))
    for item in data:
        with open(f"./html/{item['file_name']}",'rb') as f:
            content = f.read()
            file_name = item['file_name'].split("_")[-1]
            book.set_content(uid=file_name,title=file_name.split(".")[0],file_name=file_name,content=content,css=[])
    book.save()
        
        
    
        
        
    # # add metadata
    # book.set_identifier('sample123456')
    # book.set_title('Sample book')
    # book.set_language('en')
    #
    # book.add_author('Aleksandar Erkalovic')
    #
    #
    # aa = []
    # for i in item:
    #     data = item[i]
    #     content = open(data['content'], "r", encoding="utf-8").read()
    #     c1 = epub.EpubHtml(title=i,
    #                        file_name=f'{i}.xhtml',
    #                        lang='en')
    #
    #     c1.set_content(content)
    #     c1.add_item(nav_css)
    #     for img in data['img']:
    #
    #         image_content = open(img, 'rb').read()
    #         img_item = epub.EpubImage(uid=img.split("/")[-1], file_name=img, media_type='image/jpg',
    #                              content=image_content)
    #         book.add_item(img_item)
    #
    #     aa.append(
    #         c1
    #     )
    #     book.add_item(c1)
    # # add chapters to the book
    #
    # # create table of contents
    # # - add manual link
    # # - add section
    # # - add auto created links to chapters
    # style = open("./css/stylesheet.css",encoding="utf-8").read()
    # nav_css = epub.EpubItem(uid="stylesheet", file_name="css/stylesheet.css", media_type="text/css", content=style)
    # book.add_item(nav_css)
    #
    #
    # book.toc = (epub.Link('intro.xhtml', 'Introduction', 'intro'),
    #             (epub.Section('Languages'),
    #              (i for i in aa))
    #             )
    #
    # # add navigation files
    # book.add_item(epub.EpubNcx())
    # book.add_item(epub.EpubNav())
    #
    # # create spine
    # book.spine = ['nav',*aa]
    #
    # # create epub file
    # epub.write_epub('test.epub', book, {})
