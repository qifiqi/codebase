import datetime
import requests
import time
import re
import json
import pandas as pd
import execjs


# import js2py
class Highway:
    def __init__(self):
        print(1)
        self.recoverss()

    def recoverss(self):  # 请求ironsFans
        recover = self.secids()
        e = ''
        for i in recover:
            a = json.loads(i)
            e += a['code'] + ','

        jstext = '''

        function r(e) {
            if ("105" == e.substring(0, 3) || "106" == e.substring(0, 3) || "107" == e.substring(0, 3))
                return e;
            if ("NASDAQ" == e.substring(0, 6) || "nasdaq" == e.substring(0, 6))
                return "105." + e.substring(7, 999);
            if ("NYSE" == e.substring(0, 4) || "nyse" == e.substring(0, 4))
                return "106." + e.substring(5, 999);
            if ("AMEX" == e.substring(0, 4) || "amex" == e.substring(0, 4))
                return "107." + e.substring(5, 999);
            if ("HK" == e.substring(0, 2) || "hk" == e.substring(0, 2))
                return "116." + e.substring(3, 999);
            var t = e.substring(0, 1)
              , n = e.substring(0, 2)
              , r = e.substring(0, 3);
            return "5" == t || "6" == t || "9" == t ? "1." + e : 0 == e.toLowerCase().indexOf("sh") ? "1." + e.substring(2, e.length) : 0 == e.toLowerCase().indexOf("sz") ? "0." + e.substring(2, e.length) : "bk" == n.toLowerCase() ? "90." + e : "000003" == e || "000300" == e ? "1." + e : "009" == r || "126" == r || "110" == r ? "1." + e : "0." + e
        }


         function getHQSecIdByMutiCode(e) {
            for (var t = [], n = 0, o = e.split(","); n < o.length; n++) {
                var i = r(o[n]);
                t.push(i)
            }
            return t.join(",")
        }
        '''
        context1 = execjs.compile(jstext)
        secids = context1.call("getHQSecIdByMutiCode", e)
        current_milli_time = str(int(round(time.time() * 1000)))
        # secids 要变化

        # url = 'https://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&np=3&ut=a79f54e3d4c8d44e494efb8f748db291&invt=2&secids=1.603000,1.601138,0.002703,0.002400,1.603083,0.000977,0.002654,1.600050,0.002292,0.002590,1.600487,0.002261,0.002077,0.002230,0.000980,0.300475,0.002463,1.603019,0.002527,0.300364&fields=f1,f2,f3,f4,f12,f13,f14,f152,f15,f16&cb=qa_wap_jsonpCB{}'.format(
        url = 'https://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&np=3&ut=a79f54e3d4c8d44e494efb8f748db291&invt=2&secids={}&fields=f1,f2,f3,f4,f12,f13,f14,f152,f15,f16&cb=qa_wap_jsonpCB{}'.format(
            secids, current_milli_time)
        res = requests.get(url).text
        # print(res)
        lone = re.search('qa_wap_jsonpCB.*?\((.*?)\);', res).group(1)
        # print(lone)
        line = json.loads(lone)  # 将字符串转为字典
        # print(line)
        self.pack(line, recover)

    def secids(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36'}

        one = str(datetime.datetime.now().strftime('_%m_%d_%H_%M'))
        try:
            print(one)
            two = one.replace('0', '')
            four = '2023' + two
            print(two)
            print(four)
        except:
            print('当前无法转换')
            return

        url3 = 'http://gbcdn.dfcfw.com/rank/popularityList.js?type=0&sort=0&page=1&v={}'.format(four)
        packs = requests.get(url=url3, headers=headers).text
        three = re.search('.*?popularityList=\'(.*?)\'', packs).group(1)
        # print(packs)
        # print(three,123)
        suitcase = self.js_from_file('overcoat.js')
        # print(suitcase)
        # context = js2py.EvalJs()
        # context = js2py.eval_js(suitcase)
        # context.teenager(three)
        # context.execute(suitcase)
        context1 = execjs.compile(suitcase)
        result1 = context1.call("teenager", three)
        # print(result1)
        recover = re.findall('\{"code":.*?}]}', result1)

        return recover

    def pack(self, suit, recover):  # 取出想要的内容  当前排名+排名较昨日变动+代码+股票名称+新晋粉丝+铁杆粉丝

        overcoat = []  # 当前排名
        teenage = []  # 排名较昨日变动
        along = []  # 代码
        gossip = []  # 股票名称
        night = []  # 新晋粉丝
        series = []  # 铁杆粉丝
        series_of = suit['data']['diff']
        spellbind = 0

        # for t in recover:
        #     print(t)
        #     print(type(t))
        #     series1 = json.loads(t)
        #     print(series1)
        #     print(type(series1))
        # print(recover)
        # print(len(recover))
        # print(type(list(result1)))
        # print(list(result1))
        # result1.split(sep=None, maxsplit=-1)
        # print(type(result1))
        # suffer = result1[0]
        # suffer = list(result1)
        # for t in suffer:
        #     print(t)
        # series_of_s = {}
        # for i in series_of:
        #     series_of_s[i['f12']] = i

        for i in series_of:
            t = json.loads(recover[spellbind])
            # print(t)
            # print(i)
            spellbind += 1
            # da['overcoat'] = spellbind
            # da['along'] = series_of_s[t['code']]['f12']
            # da['gossip'] = series_of_s[t['code']]['f14']
            # da['teenage'] = t['changeNumber']
            # da['night'] = t['newFans']
            # da['series'] = t['ironsFans']
            overcoat.append(spellbind)
            along.append(i['f12'])
            gossip.append(i['f14'])
            teenage.append(t['changeNumber'])
            night.append(t['newFans'])
            series.append(t['ironsFans'])
        try:
            yes = pd.DataFrame(
                {'当前排名': overcoat, '排名较昨日变动': teenage, '代码': along, '股票名称': gossip, '新晋粉丝': night,
                 '铁杆粉丝': series})
            print(yes)
        except:
            print('1')

        # tom = 'http://guba.eastmoney.com/rank/'
        # yes1 = requests.get(url=tom, headers=headers).text
        # print(yes1)
        pass

    def js_from_file(slef, highway):
        tom = open(highway, mode='r').read()
        # print(tom.read())
        return tom


if __name__ == '__main__':
    outdoors = Highway()
