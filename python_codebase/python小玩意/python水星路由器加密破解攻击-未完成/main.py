import requests
from concurrent.futures import ThreadPoolExecutor

th = ThreadPoolExecutor(max_workers=32)


def securityEncode(b):
    a = "RDpbLfCPsJZ7fiv"
    e = ""
    c = "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW"
    l = 118
    n = 187

    g = len(a)
    h = len(b)
    k = len(c)
    f = g if g > h else h
    for p in range(f):
        n = l = 187
        if p >= g:
            n = ord(b[p])
        else:
            if p >= h:
                l = ord(a[p])

            else:
                l = ord(a[p])
                n = ord(b[p])

        # e += c.charAt((l ^ n) % k)
        e += c[(l ^ n) % k]
    return e


def get_pass(password):
    passwd = securityEncode(password)
    url = "http://192.168.1.1/"
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42"
    }

    data = {"method": "do", "login": {"password": passwd}}

    da = requests.post(url, head, data).json()
    print(da)
    if da.get("error_code") != -40210:
        th.shutdown()
    print(str(da.get("error_code"))+":" + password)


if __name__ == '__main__':
    get_pass("123qwe")
