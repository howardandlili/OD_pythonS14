#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
account_file = 'user.txt'
lock_file = 'account_lock.txt'
Username = 'wangwu'
Password = '789'
with open(account_file,'r') as f: #打开用户列表
    for line in f.readlines(): #遍历文档每一行
        username,password = line.strip().split() #把每一行的字符串以空格分拆，并且赋值
        if Username == username and Password == password:
            print('成功登陆')
            userpass = 'T'