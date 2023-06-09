import requests
from lxml import etree
import csv

req = requests.get('https://www.haoyunbb.com/news/3/36573.html')
req.encoding = 'utf-8'
html = etree.HTML(req.text)
aa = open('./疫情数据全国.csv', 'a+', encoding='utf-8', newline='')
csv_aa = csv.writer(aa)
csv_aa.writerow(['城市', '新增确诊', '累计确诊', '治愈', '死亡'])

shenf = html.xpath('//div[@id="art"]/div[4]/ul/li')
for i in shenf[1:]:
    name = i.xpath('./div[1]/label/text()')[0]
    add = i.xpath('./div[2]/text()')[0]
    leiji = i.xpath('./div[3]/text()')[0]
    zhiyu = i.xpath('./div[4]/text()')[0]
    kill = i.xpath('./div[5]/text()')[0]
    csv_aa.writerow([name, add, leiji, zhiyu, kill])
