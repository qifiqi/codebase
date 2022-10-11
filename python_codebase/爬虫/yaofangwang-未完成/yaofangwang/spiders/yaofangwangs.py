import scrapy
from yaofangwang.items import YaofangwangItem




class YaofangwangsSpider(scrapy.Spider):
    name = 'yaofangwangs'
    # allowed_domains = ['yaofangwang.com']
    # start_urls = [f"https://www.yaofangwang.com/catalog-1/p{i}/" for i in range(1,1156)]
    start_urls = ["https://www.yaofangwang.com/catalog-1/p1/"]




    def parse(self, response):

        def subs(s):
            font = {
                "&#x351D;": 0,
                "&#x3E73;": 1,
                "&#xB561;": 2,
                "&#x0F88;": 3,
                "&#xCC5E;": 4,
                "&#x1ECC;": 5,
                "&#xE171;": 6,
                "&#x0FFF;": 7,
                "&#x2FCF;": 8,
                "&#x2992;": 9,
            }
            ss = s.split("&")
            print(ss)
            a = [ss[0]]
            for i in ss[1:]:
                print(i)
                i = "&" + i
                for k in font.keys():
                    i = i.replace(k, str(font[k]))
                    print(i)
                else:
                    a.append(i)
            return "".join(a)

        li_list = response.css("ul.goodlist li")
        item = YaofangwangItem()
        for li in li_list:
            print(li)
            "药品图地址，价格，药品名，规格，批准文号，生产厂家"
            item['img_path'] = li.css("img.autoimg::attr(src)").extract_first()
            item['price'] = li.css("span.ybfont_ml3::text").extract_first()
            item['name'] = li.css("a.txt::text").extract_first()
            item['gge'] = li.css("p.st::text").extract_first()
            pzwh = li.css("span.ybfont::text").extract_first()
            # print(self.subs(pzwh))
            item['pzwh'] = subs(pzwh)
            item['sccj'] = li.css("p.n::text").extract_first()
            # print(item)
