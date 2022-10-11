# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/6/21 20:57
# @Author  : 符青
# @Email   : 2737454073@qq.com
# @File    : steam登录密码加密-RSA.py
# @Software: PyCharm

"""
第一步找到相关加密js,
    1.在可疑的地方加入断点
    2.找到以后查看方法和参数是不是js自定义的，若不是者去寻找相关的js，
    若是发现相关的js命名类似加密的算法的话这个时候就可以考虑复制全部的js代码
    3.缺啥补啥，变量的话，可疑直接复制为this
"""
# 第二步 找js发现是非对称的加密,要找到对应加密的公钥和私钥
import requests

urls = 'https://store.steampowered.com/login/getrsakey/'

data = {
    'donotcache': '1655818031815',
    'username': '19354adf'
}

header = {
    'Referer': 'https://store.steampowered.com/login/?redir=&redir_ssl=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44 '

}
response = requests.post(urls, data=data, headers=header).json()
mod = response['publickey_mod']
exp = response['publickey_exp']
# 第三步，开始使用python调用js execjs
print(mod, exp)

import execjs

node = execjs.get()

aa = node.compile(open('./steam.js', encoding='utf-8').read())

faname = 'pwd("{}","{}","{}")'.format('123123', mod, exp)

data = aa.eval(faname)
print(data)
