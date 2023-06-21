# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Selector
from lxml import etree


# from twisted.internet.ssl import AcceptableCiphers # 当请求出现 ssl(dh key too small) 异常时，可以尝试解该处注释
# from scrapy.core.downloader import contextfactory
# contextfactory.DEFAULT_CIPHERS = AcceptableCiphers.fromOpenSSLCipherString('DEFAULT:!DH')

# 以下补丁代码：用于预防有人可能会用 pythonw 执行 scrapy 单脚本时可能会出现的编码问题，如果直接用 python 执行该处则有无皆可。
# import io, sys; sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# 以下补丁代码：用于预防处理 “scrapy(twisted) 对极少数的某些网站返回的不规范 headers 无法处理” 的异常情况
def lineReceived(self, line):
    if line[-1:] == b'\r': line = line[:-1]
    if self.state == u'STATUS':
        self.statusReceived(line);
        self.state = u'HEADER'
    elif self.state == u'HEADER':
        if not line or line[0] not in b' \t':
            if self._partialHeader is not None:
                _temp = b''.join(self._partialHeader).split(b':', 1)
                name, value = _temp if len(_temp) == 2 else (_temp[0], b'')
                self.headerReceived(name, value.strip())
            if not line:
                self.allHeadersReceived()
            else:
                self._partialHeader = [line]
        else:
            self._partialHeader.append(line)


import twisted.web._newclient

twisted.web._newclient.HTTPParser.lineReceived = lineReceived
# 以下补丁代码：解决 idna 库过于严格，导致带有下划线的 hostname 无法验证通过的异常
import idna.core

_check_label_bak = idna.core.check_label


def check_label(label):
    try:
        return _check_label_bak(label)
    except idna.core.InvalidCodepoint:
        pass


idna.core.check_label = check_label

import re
import json
from urllib.parse import unquote, quote


class VSpider(scrapy.Spider):
    name = 'v'

    custom_settings = {
        'COOKIES_ENABLED': True,
        # Do not use automatic cookie caching(set 'dont_merge_cookies' as True in Request.meta is same)
    }
    proxy = None  # 'http://127.0.0.1:8888'

    def start_requests(self):
        def mk_url_headers(id, page):
            def quote_val(url): return re.sub(r'([\?&][^=&]*=)([^&]*)',
                                              lambda i: i.group(1) + quote(unquote(i.group(2), encoding='utf-8'),
                                                                           encoding='utf-8'), url)

            url = (
                'https://www.sslibrary.com/book/search/do'
                f'?classifyId={id}'
                f'&page={page}'
                '&pagesize=50'
                '&searchNewLib=0'
                '&fromType=portal'
            )
            url = quote_val(url)
            headers = {
                "Cookie": (
                    "JSESSIONID=1DCD207EB653124503632E2AC975826B.dsk44_web; "
                    "UID=276531478; "
                    "_d=1691849034283; "
                    "_uid=276531478; "
                    "account=; "
                    "cdmhsession=ODBjMjQ0MTAtMWIwNS00ZmFiLWFjY2MtMDI0ZjMzNzVlNGY2; "
                    "current_page_id=239443; "
                    "cx_p_token=3caf4788c87b454599248999f9cf330f; "
                    "deptid=123859; "
                    "dname=Z2ZrZHh0eXRzZw%3D%3D; "
                    "enc=4af055c1fef3b3afb52a1989ac46744f; "
                    "fid=212111; "
                    "goc=o; "
                    "lan=zh; "
                    "lo_page_index=1; "
                    "loginType=certify; "
                    "login_sign=1; "
                    "lv=0; "
                    "mh_sign=e4e642f739277d7db7ad84864aecba3d; "
                    "msign=128936497444331; "
                    "sfid=123859; "
                    "uf=da0883eb5260151e7077b7c30a1440ec56f6e14d04bccbdc43108374a467650de471e50e8bd66f7fd2d6d58f323e2ef193a156299638e1035751d0b85711d6322158a1dc81ff45ef98cbd0d4bfed09f90d8a4c92b12beb4b2375e8419be99bb7bcf800c8d0574000bb0d85ccc4344404; "
                    "uname=20230301; "
                    "username=111%2e18%2e96%2e8; "
                    "vc2=C4757943FA3F18F3870E87CA04F4252A; "
                    "vc3=enF5AxMH7JB%2F6j%2FkGrasPplTNK8az1ysO2kYyL%2BpWb0zlwlUIduGfLj97lhVL5EkN0m9SxRKQeQodP52pu2OAumqs6vQv2PoV1jgHrylHBAsMe8cGk%2Bitm4PfjPuyLC%2BitEo0tFY%2BCxA59dIEwDEVP%2B1x4isSM9ptKcvjnDm2T4%3D34fc5d36d12390a2bc1b16b1be15edd1; "
                    "vc=3AF55379F285F92DC01BCFDA624FD9A0; "
                    "website_fid=187742; "
                    "website_fid_login=0; "
                    "website_id=143287; "
                    "xxtenc=bf414ec5c5150abb4dbf27aa30fcb01a; "
                    "DSSTASH_LOG=C%5f34%2dUN%5f123859%2dUS%5f%2d1%2dT%5f1691855251428"
                ),
                "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Microsoft Edge\";v=\"115\", \"Chromium\";v=\"115\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"Windows\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
            }
            return url, headers

        for i in range(1, 23):
            i = str(i).zfill(2)
            url, headers = mk_url_headers(id=i, page=1)
            meta = {}
            meta['proxy'] = self.proxy
            meta['num'] = 0
            meta['page'] = 1
            meta['id'] = i
            r = Request(
                url,
                headers=headers,
                callback=self.parse,
                meta=meta,
            )
            yield r
            break

    def parse(self, response):
        # If you need to parse another string in the parsing function.
        # use "etree.HTML(text)" or "Selector(text=text)" to parse it.
        # ps. if you use "etree.HTML(text)" and text startswith '<?xml version="1.0" encoding="utf-8"?>'
        # pls use "etree.HTML(re.sub(r'^ *<\?xml[^<>]+\?>', '', text))"

        def mk_url_headers(id, page):
            def quote_val(url): return re.sub(r'([\?&][^=&]*=)([^&]*)',
                                              lambda i: i.group(1) + quote(unquote(i.group(2), encoding='utf-8'),
                                                                           encoding='utf-8'), url)

            url = (
                'https://www.sslibrary.com/book/search/do'
                f'?classifyId={id}'
                f'&page={page}'
                '&pagesize=50'
                '&searchNewLib=0'
                '&fromType=portal'
            )
            url = quote_val(url)
            headers = {

                "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Microsoft Edge\";v=\"115\", \"Chromium\";v=\"115\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"Windows\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
            }
            return url, headers

        id = response.meta["id"]
        page = response.meta["page"]
        num = response.meta["num"]
        print(response.text)
        # data = response.json()["data"]
        #
        # num += int(len(data["result"]))
        # for i in data:
        #     pass
        #
        # if num >= int(data["total"]):
        #     return
        #
        # url, headers = mk_url_headers(id=id, page=page)
        # meta = {}
        # meta['proxy'] = self.proxy
        #
        # meta['num'] = num
        # meta['page'] = page + 1
        # meta['id'] = id
        # r = Request(
        #     url,
        #     headers = headers,
        #     callback = self.parse,
        #     meta = meta,
        # )
        # yield r


# 配置在单脚本情况也能爬取的脚本的备选方案，使用项目启动则下面的代码无效
if __name__ == '__main__':
    import os, time
    from scrapy.crawler import CrawlerProcess

    timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())  # 年月日_时分秒
    filename = 'v{}.json'.format(timestamp)  # 这是输出文件名字（解开 'FEED_URI' 配置注释生效）
    jobdir = 'JOBDIR/NdbTlhVnZm'  # 这是队列信息地址（解开 'JOBDIR'   配置注释生效）

    p = CrawlerProcess({
        'TELNETCONSOLE_ENABLED': False,  # 几乎没人使用到这个功能，直接关闭提高爬虫启动时间
        'MEDIA_ALLOW_REDIRECTS': True,  # 允许图片下载地址重定向，存在图片下载需求时，请尽量使用该设置
        'LOG_LEVEL': 'INFO',  # DEBUG , INFO , WARNING , ERROR , CRITICAL
        # 'JOBDIR':                   jobdir,     # 解开注释则增加断点续爬功能
        # 任务队列、任务去重指纹、任务状态存储空间(简单来说就是一个文件夹)
        'FEED_URI': filename,  # 下载数据到文件
        'FEED_EXPORT_ENCODING': 'utf-8',  # 在某种程度上，约等于 ensure_ascii=False 的配置选项
        # 'FEED_FORMAT':              'json',     # 下载的文件格式，不配置默认以 jsonlines 方式写入文件，
        # 支持的格式 json, jsonlines, csv, xml, pickle, marshal
        # 'DOWNLOAD_TIMEOUT':         8,          # 全局请求超时，默认180。也可以在 meta 中配置单个请求的超时( download_timeout )
        # 'DOWNLOAD_DELAY':           1,          # 全局下载延迟，这个配置相较于其他的节流配置要直观很多
    })
    p.crawl(VSpider)
    p.start()
