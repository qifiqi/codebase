import csv
import random

import feapder
import datetime
import time


class AirSpiderDemo(feapder.AirSpider):
    def start_requests(self):
        category1 = 16750
        category2 = 16755
        category3 = [16806, 16809, 16810, 16812, 16815]
        searchUUID = '6b1d113b988148978a2115e581e21956'
        for i in category3:
            for j in range(1, 101):
                category3 = i
                page = j
                aa = int(time.time() * 1000)
                time.sleep(0.01)
                url = "https://api.m.jd.com/api"
                sing = ''
                params = {
                    "functionId": "unionSearch",
                    "appid": "unionpc",
                    "_": f"{aa}",
                    "loginType": "3",
                    "uuid": "1679216141753694916940",
                    "x-api-eid-token": "jdd03HQRC6DQIP3LKJQR2NLC44XTXZU3OIBVKNLRLRP6XFYCCTCEUR2KZ3RAQWXXTJ3ZCRH65F3JNZGTVKDQGBQ6LPMERKEAAAAMILOST77YAAAAADD5NUL6B7JQC5EX",
                    "h5st": f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]};5335582226479205;586ae;tk03wb01a1c0618nUQXArXp1n6gIcnWTuEFcVgNaiNSghPZKG1gTQgGtsB-frP9P1oW7EapYNqN6wQo9e9_Jq-X28qpM;{sing};3.1;{int(time.time() * 1000)};24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e355076cc27b11bb228be53f32ed205652f7009c1b62a0650a84c3f3b59681b5b54f2eefb56bdb382fa0a18cfb338e4255a6d5b0655a5df1b1ef27db99ae19ec0cd520a0e3a66752826c059a3929fbb8c9",
                    "body": '{"funName":"search","version":"v3","source":20310,"param":{"pageNo":' + str(
                        page) + ',"pageSize":60,"searchUUID":"' + searchUUID + '","bonusIds":null,"category1":' + str(
                        category1) + ',"category2":' + str(category2) + ',"category3":' + str(
                        category3) + ',"deliveryType":null,"wlRate":null,"maxWlRate":null,"fromPrice":null,"toPrice":null,"hasCoupon":null,"isHot":null,"isNeedPreSale":null,"isPinGou":null,"isZY":null,"isCare":null,"lock":null,"orientationFlag":null,"sort":null,"sortName":null,"keyWord":"","searchType":"st3","keywordType":"kt0"},"clientPageId":"jingfen_pc"}'
                }
                yield feapder.Request(url,
                                      params=params,
                                      method="GET",
                                      timeout=(5, 5),
                                      aa_date={'category1': category1,
                                               'category2': category2,
                                               'category3': category3,
                                               'page': page
                                               })
                time.sleep(random.randint(3, 10))
            time.sleep(random.randint(20, 40))
                # break
            # break

    def start_callback(self):
        self._files = open("./demo2.csv", "a+", encoding="utf-8", newline="")
        self.file_csv = csv.writer(self._files)
        self.file_csv.writerow(['一级分类', '二级分类', '三级分类', '商品id', '好评数'])

    def end_callback(self):
        self._files.close()

    def download_midware(self, request):
        request.headers = {
            "authority": "api.m.jd.com",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "origin": "https://union.jd.com",
            "pragma": "no-cache",
            "referer": "https://union.jd.com/",
            "sec-ch-ua": "^\\^Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50",
            "x-referer-page": "https://union.jd.com/proManager/index",
            "x-rp-client": "h5_1.0.0"
        }
        request.cookies = {
            "__jdu": "1679216141753694916940",
            "shshshfpa": "d46abd37-6807-9ec6-6151-128aeea1249a-1679216141",
            "shshshfpx": "d46abd37-6807-9ec6-6151-128aeea1249a-1679216141",
            "shshshfpb": "ryl9pVLl5_EF0RwHBtK4AVg",
            "shshshfp": "db88057f58bfbbf42cd2ededafdb835b",
            "ipLoc-djd": "18-1555-29463-29710",
            "pinId": "pd3Wh5ql1XnEQp4btAX0gQ",
            "unick": "jd_onUrLWCEMwRo",
            "_tp": "BnzamxlgayNrcNXXe^%^2F^%^2FjUA^%^3D^%^3D",
            "_pst": "jd_onUrLWCEMwRo",
            "user-key": "787f7d90-7411-4d85-accb-3b25250355a6",
            "unpl": "JF8EALBnNSttCh9TDBMGGkdFQllTW1RaQh9Qb2RVAA5bGQQMH1ZIE0V7XlVdXxRKEx9vYhRUXlNKVw4ZCisSEXteU11bD00VB2xXXAQDGhUQR09SWEBJJV9UXFkBTxIHbmAFZG1bS2QFGjIbFRZDXlRZXQ1LEQdtYA1RVVhMXAAaMhoiF3ttZFheCU0fM25XBGQfDBdUABMEH18QTFtcXV0PSxIDaWMHU1VdQ1QCEwcaIhF7Xg",
            "__jdv": "122270672^|haosou-search^|t_262767352_haosousearch^|cpc^|31358545061_0_ce68950dd85648c89b12aeb2ca85eb0d^|1684036960111",
            "3AB9D23F7A4B3C9B": "HQRC6DQIP3LKJQR2NLC44XTXZU3OIBVKNLRLRP6XFYCCTCEUR2KZ3RAQWXXTJ3ZCRH65F3JNZGTVKDQGBQ6LPMERKE",
            "__jda": "209449046.1679216141753694916940.1679216142.1685095792.1685164734.11",
            "__jdc": "209449046",
            "wlfstk_smdl": "zr1aad857oyn16xx1cwoxjdo1fj3zm2z",
            "TrackID": "12r5zAMCAE3RvLTC4YZiIJ27qyrePQMZAwUhIWDbuUe3gjqhobwdk_A54VgzUgZsJqzblMYeCB9_-JehyzhTvgoVWfm415s9p-xj432R2oS8E-NaQ28Qeu2fOa0YdOngE",
            "flash": "2_wTSPDVF1L0-Cp2x9qKjxop1dhP9YwZv1rdYqrDfjk-nAHxlXXfdBr-SbI8F7LR3dNANDKd2GuRrFD5MPi53MyLlIoz6ev7-8Uq9lIHYZp6D*",
            "pin": "jd_onUrLWCEMwRo",
            "ceshi3.com": "000",
            "3AB9D23F7A4B3CSS": "jdd03HQRC6DQIP3LKJQR2NLC44XTXZU3OIBVKNLRLRP6XFYCCTCEUR2KZ3RAQWXXTJ3ZCRH65F3JNZGTVKDQGBQ6LPMERKEAAAAMILPHKDCYAAAAADGB27JGCQP627IX",
            "RT": "^\\^z=1&dm=jd.com&si=0bf76fj1t25a&ss=li5jkl9z&sl=k&tt=e5km&ld=23fpz&ul=1m6f8&hd=1m6fh&nu=881302e8cb8459f97a56d4285ada2b56&cl=1s2ig^^",
            "thor": "7F0969E595AD350DB8D4722E0BECE00424328C5108223992858BF8DF0654EBFEFB2507590E487990E5227405A4DC10DC32B44F890B7F28CC53FA1C435B961844279F839B881671BC8DC5071F21D17F1C374B68F4FD69A0B452DE63319403505976107FBAC2DABB5BBC02059A403BD4484B70701EF21A0E666CEC861FE3BB0B018AF9D1431600108CDDE327644B958A2162C85BBCB9C6DA556C78C755F7A2BE3F",
            "__jdb": "209449046.30.1679216141753694916940^|11.1685164734"
        }
        return request

    def parse(self, request, response):
        aa_data = request.aa_date
        for i in response.json["data"]["skuPage"]["result"]:
            self.file_csv.writerow([
                aa_data["category1"],
                aa_data["category2"],
                aa_data["category3"],
                i["skuId"],
                i["goodComments"],
            ])
        print(aa_data)


if __name__ == "__main__":
    AirSpiderDemo(thread_count=3).start()
    # pass
