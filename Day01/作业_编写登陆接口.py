#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
要求：
1.输入用户名密码
2.认证成功后显示欢迎信息
3.输错三次后锁定
'''
#########################
'''
readme
    这是一个登陆接口的项目，首要要求输入用户名和密码，如果都正确则打印欢迎语句，
    否则要求重新输入，超过三次失败就会被锁定。
'''
account_file = 'user.txt'
lock_file = 'account_lock.txt'
userpass = 'F'
count = 0
while userpass == 'F' :
    Username = input('输入用户名：')
    Password = input('输入密码')
    with open(lock_file,'r') as f: #打开锁定用户列表
        for line in f.readlines(): #遍历文档每一行
            username = line.strip() #把每一行的字符串以空格分拆，并且赋值
            if Username == username:
                print('您的账户被锁定')
                userpass = 'F'
    with open(account_file,'r') as f: #打开用户列表
        for line in f.readlines(): #遍历文档每一行
            username,password = line.strip().split() #把每一行的字符串以空格分拆，并且赋值
            if Username == username and Password == password:
                print('成功登陆')
                userpass = 'T'
            else:
                print('您的账户或者密码错误')
                userpass = 'F'
    if userpass == 'F':
        continue
    else:
        break
else:
    print("错误次数过多，账号被锁")
    with open(lock_file,'a+') as L:
        L.write('\n')
        L.write(Username)