import sys

import requests
from requests.cookies import cookiejar_from_dict
from requests.structures import CaseInsensitiveDict

session = requests.session()
session.headers = CaseInsensitiveDict({
    "authority": "www.sslibrary.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.sslibrary.com/",
    "sec-ch-ua": "^\\^Not/A)Brand^^;v=^\\^99^^, ^\\^Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
})
session.cookies = cookiejar_from_dict({
    "uname": "20230301",
    "lv": "0",
    "fid": "212111",
    "_uid": "276531478",
    "uf": "da0883eb5260151e7077b7c30a1440ec56f6e14d04bccbdc43108374a467650de471e50e8bd66f7fd2d6d58f323e2ef193a156299638e1035751d0b85711d6322158a1dc81ff45ef98cbd0d4bfed09f90d8a4c92b12beb4b2375e8419be99bb7bcf800c8d0574000bb0d85ccc4344404",
    "_d": "1691849034283",
    "UID": "276531478",
    "vc": "3AF55379F285F92DC01BCFDA624FD9A0",
    "vc2": "C4757943FA3F18F3870E87CA04F4252A",
    "vc3": "enF5AxMH7JB^%^2F6j^%^2FkGrasPplTNK8az1ysO2kYyL^%^2BpWb0zlwlUIduGfLj97lhVL5EkN0m9SxRKQeQodP52pu2OAumqs6vQv2PoV1jgHrylHBAsMe8cGk^%^2Bitm4PfjPuyLC^%^2BitEo0tFY^%^2BCxA59dIEwDEVP^%^2B1x4isSM9ptKcvjnDm2T4^%^3D34fc5d36d12390a2bc1b16b1be15edd1",
    "cx_p_token": "3caf4788c87b454599248999f9cf330f",
    "xxtenc": "bf414ec5c5150abb4dbf27aa30fcb01a",
    "dname": "Z2ZrZHh0eXRzZw^%^3D^%^3D",
    "sfid": "123859",
    "username": "111^%^2e18^%^2e96^%^2e8",
    "account": "",
    "loginType": "certify",
    "deptid": "123859",
    "website_id": "143287",
    "website_fid": "187742",
    "website_fid_login": "0",
    "lan": "zh",
    "goc": "o",
    "login_sign": "1",
    "current_page_id": "239443",
    "mh_sign": "e4e642f739277d7db7ad84864aecba3d",
    "lo_page_index": "1",
    "cdmhsession": "ODBjMjQ0MTAtMWIwNS00ZmFiLWFjY2MtMDI0ZjMzNzVlNGY2",
    "JSESSIONID": "1DCD207EB653124503632E2AC975826B.dsk44_web",
    "msign": "128936497444331",
    "enc": "4af055c1fef3b3afb52a1989ac46744f",
    "DSSTASH_LOG": "C^%^5f34^%^2dUN^%^5f123859^%^2dUS^%^5f^%^2d1^%^2dT^%^5f1691855251428"
})


# url = "https://www.sslibrary.com/book/search"
# params = {
#     "classifyId": 1,
#     "classifyName": "^%^E9^%^A9^%^AC^%^E5^%^85^%^8B^%^E6^%^80^%^9D^%^E4^%^B8^%^BB^%^E4^%^B9^%^89^%^E3^%^80^%^81^%^E5"
#                     "^%^88^%^97^%^E5^%^AE^%^81^%^E4^%^B8^%^BB^%^E4^%^B9^%^89^%^E3^%^80^%^81^%^E6^%^AF^%^9B^%^E6^%^B3"
#                     "^%^BD^%^E4^%^B8^%^9C^%^E6^%^80^%^9D^%^E6^%^83^%^B3^%^E3^%^80^%^81^%^E9^%^82^%^93^%^E5^%^B0^%^8F"
#                     "^%^E5^%^B9^%^B3^%^E7^%^90^%^86^%^E8^%^AE^%^BA",
#     "fromType": "portal"
# }
# response = session.get(url, params=params)
#
# print(response)
#
# url = "https://www.sslibrary.com/book/search/do"
# data = {
#     "sw": "",
#     "allsw": "",
#     "searchtype": "",
#     "classifyId": '01',
#     "isort": "",
#     "field": "",
#     "jsonp": "",
#     "showcata": "",
#     "expertsw": "",
#     "bCon": "",
#     "page": 1,
#     "pagesize": 10,
#     "sign": "",
#     "enc": "",
#     "searchNewLib": 0,
#     "fromType": "portal"
# }
# response = requests.post(url, data=data)
# response = session.post(url, data=data)
# response = session.get(url, data=data, verify=False)
class pool:
    import time, queue, traceback, builtins, functools
    from threading import Thread, RLock, current_thread, main_thread
    orig_func = {}
    _org_print = print
    lock = RLock()

    class KillThreadParams(Exception):
        pass

    _monitor = None
    _monitor_run_num = {}
    _pool_queue = {}
    _pool_func_num = {}

    def __init__(self, pool_num=None, gqueue='v', monitor=True):
        if gqueue not in self._pool_queue:
            self._pool_queue[gqueue] = pool.queue.Queue()
        self._pool = self._pool_queue[gqueue]
        pool._patch_print()
        if monitor: self.main_monitor()
        if gqueue not in self._monitor_run_num:
            self._monitor_run_num[gqueue] = pool.queue.Queue()
        num = self._auto_pool_num(pool_num)
        if gqueue not in self._pool_func_num:
            self._pool_func_num[gqueue] = num
            self._run(num, gqueue)
        else:
            if pool_num is not None:
                self.change_thread_num(num, gqueue)

    def __call__(self, func):
        pool.orig_func[func.__name__] = func

        @pool.functools.wraps(func)
        def _run_threads(*args, **kw): self._pool.put((func, args, kw))

        return _run_threads

    @classmethod
    def change_thread_num(self, num, gqueue='v'):
        if gqueue in self._pool_func_num:
            x = self._pool_func_num[gqueue] - num
            if x < 0: self._run(abs(x), gqueue)
            if x > 0: [self._pool_queue[gqueue].put(self.KillThreadParams) for _ in range(abs(x))]
            self._pool_func_num[gqueue] = num

    @classmethod
    def main_monitor(self):
        def _func():
            while True:
                pool.time.sleep(.25)
                if not pool.main_thread().isAlive() and all(map(lambda i: i.empty(), self._monitor_run_num.values())):
                    self.close_all()
                    break

        if not self._monitor:
            self._monitor = pool.Thread(target=_func, name="MainMonitor")
            self._monitor.start()

    @classmethod
    def close_by_gqueue(self, gqueue='v'):
        self.change_thread_num(0, gqueue)

    @classmethod
    def close_all(self):
        for i in self._pool_func_num: self.change_thread_num(0, i)

    @classmethod
    def wait(self, gqueue='v'):
        while self.check_stop(gqueue): pool.time.sleep(.25)

    @classmethod
    def check_stop(self, gqueue='v'):
        return self._monitor_run_num[gqueue].qsize() or self._pool_queue[gqueue].qsize()

    @staticmethod
    def atom(func):
        def _atom(*arg, **kw):
            with pool.lock: return func(*arg, **kw)

        return _atom

    @staticmethod
    def _patch_print():
        pool.builtins.print = pool._new_print

    @staticmethod
    def _new_print(*arg, **kw):
        with pool.lock: pool._org_print("[{}]".format(pool.current_thread().getName().center(13)), *arg, **kw)

    @staticmethod
    def _auto_pool_num(num):
        if not num:
            try:
                from multiprocessing import cpu_count
                num = cpu_count()
            except:
                print("cpu_count error. use default num 4.")
                num = 4
        return num

    @classmethod
    def _run(self, num, gqueue):
        def _pools_pull():
            ct = pool.current_thread()
            ct.setName("{}_{}".format(ct.getName(), gqueue))
            while True:
                v = self._pool_queue[gqueue].get()
                if v == self.KillThreadParams: return
                try:
                    func, args, kw = v
                    self._monitor_run_num[gqueue].put('V')
                    func(*args, **kw)
                except BaseException as e:
                    print(pool.traceback.format_exc())
                finally:
                    self._monitor_run_num[gqueue].get('V')

        for _ in range(num): pool.Thread(target=_pools_pull).start()


f = open("a.json", "a+", encoding="utf-8")
import json
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

t = ThreadPoolExecutor()
t.shutdown(wait=True)
q = Queue()


@pool(22, gqueue='h')  # 开启线程池组，指定名字为 'h'，线程数量为3
def aa(meta):
    id = meta["id"]
    page = meta["page"]
    num = meta["num"]
    url = f'https://www.sslibrary.com/book/search/do?classifyId={str(id).zfill(2)}&page={page}&pagesize=50&searchNewLib=0&fromType=portal'
    if num == 0: print(url)
    response = session.get(url=url, verify=False)

    data = response.json()["data"]

    num += int(len(data["result"]))
    print(url + "-" * 20 + str(num))
    q.put([json.dumps(i, ensure_ascii=False) + "\n" for i in data['result']])

    if num >= int(data["total"]):
        return

    aa(meta={"id": id, "page": page + 1, "num": num})


#

for i in range(1, 23):
    # t.submit(aa, {"id": i, "page": 1, "num": 0})
    aa({"id": i, "page": 1, "num": 0})
    # break
pool.wait(gqueue='h')  # 等待函数 func2 在 gqueue='h' 的“线程池组”里面全部执行完
aa = True

while aa:
    print(q.qsize())
    if q.qsize() == 0:
        aa = False
    else:
        f.writelines(q.get())
        f.flush()
f.close()
print("ok")
sys.exit()