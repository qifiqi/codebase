# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/11/1513:49
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : del_emilsfi.py
__author__ = 'Small Fu'

import poplib

#输入邮件地址, 口令和POP3服务器地址:

email_server = poplib.POP3_SSL("pop.qq.com", port=995)
email_server.user("2737454073@qq.com")
email_server.pass_("urtmpugttsmpddje")
#获取邮件数量和大小
# list()返回所有邮件的编号:
resp, mails, octets = email_server.list()
print(resp,mails,octets)
# 遍历所有的邮件
for i in range(1, int(mails[0].decode().split(" ")[-1])):
    # 通过retr(index)读取第index封邮件的内容；这里读取最后一封，也即最新收到的那一封邮件
    print(i)
    resp, lines, octets = email_server.retr(i)
    # lines是邮件内容，列表形式使用join拼成一个byte变量
    email_content = b'\r\n'.join(lines)
    print(email_content)
    # server.dele(i+1)
#保存并退出服务
email_server.quit() # 删除邮件在quit后才能保存



