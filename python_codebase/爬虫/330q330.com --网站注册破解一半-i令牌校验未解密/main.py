import hashlib
import json
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import urllib.parse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

t = {
    "username": "qweqweqwe",
    "password": "123qweasd",
    "confirm_password": "123qweasd",
    "realname": "",
    "r_type": 2,
    "tel": "",
    "type": 1,
    "token": "CN31_42a_0ki.Dg4MBNZqdkw1Ad6YtsKAZVbgqhftqhB14HgYlFCJ5cba_pbRb.tyt4kVH_KZkRoPGwc81XefAuKRb4kOJnwPN-AgQJXpCaK9VTrfy2vgcTaZQwwxwqL5pNNC_.UtereojLrAYbuprYcZVjRZXNqqq5PWacad6B1fffPNS9YvXI8ySS_9TDV_kGrPsCCXCf2RswfgNB6CUUy7tt4A9yeTVW6CVac9OPLVpnLk.dm1Vt17HMSKcX9uXytr9BbyNGSQmD2b8ir4r_7YmqNb5uWd9BXDdi5MdBPLEQl_1riefVh9iLi7kwEPsaoQeyx-k_TZQ1BKRBDtKP97QMxQi0xKx95yh7W_FmPMi0VLq.EAPX1UyeOxO8jxQFvg1vJsmWTlLWtGa01pEl8EnlR0Vvcnbzv.A_Ghl-qwQp7Dfvje4xXP0rpavVWMqFy5gZLb7GBEn5.UC-1-xyJGBd_o4-hxCMZO6ls9vwzXZ.0216KfwdgescZozqc3",
    "tpl": 5
}
i = 'zIgK9zsqGI72bMGBx2BxMH9P'
t_time = (time.time() * 1000).__int__()
s = '12345678ABCDEFGH'


def sort(obj):
    # 对象排序函数，将字典中的元素按照键名从小到大排列
    if isinstance(obj, dict):
        # 如果 obj 是字典类型，那么按照键名排序
        return sorted(((k, sort(v)) for k, v in obj.items()), key=lambda x: x[0])
    elif isinstance(obj, list) or isinstance(obj, tuple):
        # 如果 obj 是列表或元组类型，那么将其中的元素按照键名排序
        return [sort(x) for x in obj]
    else:
        # 其他类型直接返回
        return obj


def serialize(obj):
    # 对象序列化函数，将对象转换为字符串形式，并按照键名排序
    if isinstance(obj, dict):
        # 如果 obj 是字典类型，那么按照键名排序并连接成字符串
        return '&'.join('{}={}'.format(k, serialize(v)) for k, v in sort(obj))
    elif isinstance(obj, list) or isinstance(obj, tuple):
        # 如果 obj 是列表或元组类型，那么将其中的元素按照键名排序并连接成字符串
        return ','.join(map(serialize, obj))
    else:
        # 其他类型直接返回字符串形式
        return str(obj)

def sign(t, e, i, o):
    # 对象签名函数，将对象和三个额外属性进行合并，并进行编码和加密操作
    l = {**t, "sign_timestamp": e, "sign_aeskey": i, "sign_uri": o}
    u = sort(l)
    d = []
    for k, v in u:
        if isinstance(v, dict) or isinstance(v, list):
            e = serialize(v)
        else:
            e = str(v)
        d.append("{}={}".format(k, e))
    v = "&".join(d)
    v = urllib.parse.quote(v).replace("/", "%2F")
    return hashlib.sha1(v.encode('utf-8')).hexdigest()

def i_d(t, e, s):
    key = e.encode('utf-8')
    iv = s.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(t.encode('utf-8'), AES.block_size)
    cipher_text = cipher.encrypt(padded_text)
    encoded_text = base64.b64encode(cipher_text).decode('utf-8')
    return encoded_text

def rsa_encrypt(t, e):
    # 将公钥字符串转换为 RSA 公钥对象
    public_key = RSA.import_key(t)
    # 使用 RSA 公钥对象创建 PKCS1_v1_5 加密器
    cipher = PKCS1_v1_5.new(public_key)
    # 对明文进行加密
    encrypted_text = cipher.encrypt(e.encode('utf-8'))
    # 对加密结果进行 Base64 编码
    encoded_text = base64.b64encode(encrypted_text).decode('utf-8')
    return encoded_text

u = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+/jm7adLHn/cUaIsuuAQDlWmp5TsCdBrsrGZi/FnVVnMG0pep8Ph4sycEow8e23bRbWIjMBGSSRg4DScPPNN/ZO6NmZd9WWuNFMZ8A8Dv0TB0T78nWWtDkJ12lyRwnV75gGewlc/hR61z9OFtMk5wtOMujsJOGz73mronXW88dQIDAQAB
-----END PUBLIC KEY-----"""
data = {
    "t": t_time,
    "s": sign(t, t_time, i, '/member/user/register'),
    "d": i_d(json.dumps(t), i, s),
    "k": rsa_encrypt(u, f'"{i}"')
}
print(data)
