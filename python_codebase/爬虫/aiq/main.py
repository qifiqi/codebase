# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Selector
from lxml import etree

# 以下补丁代码：用于预防有人可能会用 pythonw 执行 scrapy 单脚本时可能会出现的编码问题，如果直接用 python 执行该处则有无皆可。
# import io, sys; sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# 以下补丁代码：用于预防处理 “scrapy(twisted) 对极少数的某些网站返回的不规范 headers 无法处理” 的异常情况
def lineReceived(self, line):
    if line[-1:] == b'\r': line = line[:-1]
    if self.state == u'STATUS': self.statusReceived(line); self.state = u'HEADER'
    elif self.state == u'HEADER':
        if not line or line[0] not in b' \t':
            if self._partialHeader is not None:
                _temp = b''.join(self._partialHeader).split(b':', 1)
                name, value = _temp if len(_temp) == 2 else (_temp[0], b'')
                self.headerReceived(name, value.strip())
            if not line: self.allHeadersReceived()
            else: self._partialHeader = [line]
        else: self._partialHeader.append(line)
import twisted.web._newclient
twisted.web._newclient.HTTPParser.lineReceived = lineReceived
# 以下补丁代码：解决 idna 库过于严格，导致带有下划线的 hostname 无法验证通过的异常
import idna.core
_check_label_bak = idna.core.check_label
def check_label(label):
    try: return _check_label_bak(label)
    except idna.core.InvalidCodepoint: pass
idna.core.check_label = check_label

import re
import json
from urllib.parse import unquote, quote

class VSpider(scrapy.Spider):
    name = 'v'

    custom_settings = {
        'COOKIES_ENABLED': False,  # Do not use automatic cookie caching(set 'dont_merge_cookies' as True in Request.meta is same)
    }
    proxy ='http://127.0.0.1:7890'
    # proxy =None

    def start_requests(self):
        def mk_url_headers():
            def quote_val(url): return re.sub(r'([\?&][^=&]*=)([^&]*)', lambda i:i.group(1)+quote(unquote(i.group(2),encoding='utf-8'),encoding='utf-8'), url)
            url = (
                'https://vip.aqdk229.com:2096/videos/index/1'
            )
            url = quote_val(url)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
            }
            return url,headers
        url,headers = mk_url_headers()
        meta = {}
        meta['proxy'] = self.proxy
        r = Request(
                url,
                headers  = headers,
                callback = self.parse,
                meta     = meta,
            )
        yield r

    def parse(self, response):
        # If you need to parse another string in the parsing function.
        # use "etree.HTML(text)" or "Selector(text=text)" to parse it.
        # ps. if you use "etree.HTML(text)" and text startswith '<?xml version="1.0" encoding="utf-8"?>'
        # pls use "etree.HTML(re.sub(r'^ *<\?xml[^<>]+\?>', '', text))"
        def mk_url_headers(url):
            def quote_val(url): return re.sub(r'([\?&][^=&]*=)([^&]*)',
                                              lambda i: i.group(1) + quote(unquote(i.group(2), encoding='utf-8'),
                                                                           encoding='utf-8'), url)

            url = quote_val(url)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
            }
            return url, headers

        sel = Selector(response)
        for item in sel.xpath("//div[@class='col-xlg videos-item']"):
            d = {}
            d['data-video-id'] = item.xpath("./div/@data-video-id").get('')
            d['data-video-title'] = item.xpath(".//a[@class='thumbnail-cover-link']/@alt").get('')
            href = response.urljoin(item.xpath(".//a[@class='thumbnail-cover-link']/@href").get(''))
            d['data-video-href'] = href
            d['data-video-img'] = item.xpath('.//img/@src').get('')
            d['desc'] = " ".join([i.strip() for i in item.xpath('.//div[@class="video-metadata-line"]//text()').getall()])
            url,headers = mk_url_headers(href)
            meta = {}
            meta['d'] = d
            meta['proxy'] = self.proxy
            r = Request(
                    url,
                    headers  = headers,
                    callback = self.parse_item,
                    meta     = meta,
                )
            yield r
        next_href = sel.xpath("//a[@class='older-posts']/@href").get('')
        if next_href:
            next_href = response.urljoin(next_href)
            url, headers = mk_url_headers(next_href)
            meta = {}
            meta['proxy'] = self.proxy
            r = Request(
                url,
                headers=headers,
                callback=self.parse,
                meta=meta,
            )
            yield r

    def parse_item(self, response):
        d = response.meta['d']
        mp4_url_m3u8 = response.xpath('/html/body/script[8]/text()').get().split('url: "')[-1].split('",')[0]
        bq = response.xpath('/html/body/section/div[2]/div[2]/div[4]/div/div[4]/p/a/button/text()').getall()
        d['mp4_url_m3u8'] = mp4_url_m3u8
        d['bq'] = bq
        d['item_url'] = response.url
        yield d


# 配置在单脚本情况也能爬取的脚本的备选方案，使用项目启动则下面的代码无效
if __name__ == '__main__':
    import os, time
    from scrapy.crawler import CrawlerProcess
    timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime()) # 年月日_时分秒
    filename = 'v{}.json'.format(timestamp) # 这是输出文件名字（解开 'FEED_URI' 配置注释生效）
    jobdir   = 'JOBDIR/tjUolxwDJH'          # 这是队列信息地址（解开 'JOBDIR'   配置注释生效）

    p = CrawlerProcess({
        'TELNETCONSOLE_ENABLED':    False,        # 几乎没人使用到这个功能，直接关闭提高爬虫启动时间
        'MEDIA_ALLOW_REDIRECTS':    True,         # 允许图片下载地址重定向，存在图片下载需求时，请尽量使用该设置
        'LOG_LEVEL':                'INFO',       # DEBUG , INFO , WARNING , ERROR , CRITICAL
        # 'JOBDIR':                   jobdir,     # 解开注释则增加断点续爬功能
                                                  # 任务队列、任务去重指纹、任务状态存储空间(简单来说就是一个文件夹)
        'FEED_URI':                 filename,   # 下载数据到文件
        'FEED_EXPORT_ENCODING':     'utf-8',    # 在某种程度上，约等于 ensure_ascii=False 的配置选项
        # 'FEED_FORMAT':              'json',     # 下载的文件格式，不配置默认以 jsonlines 方式写入文件，
                                                  # 支持的格式 json, jsonlines, csv, xml, pickle, marshal
        # 'DOWNLOAD_TIMEOUT':         8,          # 全局请求超时，默认180。也可以在 meta 中配置单个请求的超时( download_timeout )
        # 'DOWNLOAD_DELAY':           1,          # 全局下载延迟，这个配置相较于其他的节流配置要直观很多
    })
    p.crawl(VSpider)
    p.start()
