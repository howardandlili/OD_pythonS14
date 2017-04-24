#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
作业要求：
1.输入用户密码
2.认证后显示欢迎信息
3.输错三次后锁定
'''
##############################
'''
readme:
这是一个登陆接口脚本，要求输入正确的用户名和密码，如果输入三次失败后将被锁定。
现在还有一个BUG就是三次输入错误的时候只会调取最一次的用户名来锁定
'''
account_file = 'user.txt'
lock_file = 'account_lock.txt'
userpass = 'F'
count = 0
while userpass == 'F' and count <3:
    Username = input('输入用户名：')
    Password = input('输入密码：')
    count +=1
    with open(lock_file,'r') as f: #打开锁定用户列表
        for line in f.readlines(): #遍历文档每一行
            username = line.strip() #把每一行的字符串以空格分拆，并且赋值
            if Username == username: #判断用户是否在锁表中
                print('您的账户被锁定')
                userpass = 'L'
                break
    if userpass == 'L':#当被标记为L时跳出white循环
        break
    with open(account_file,'r') as f: #打开用户列表
        for line in f.readlines(): #遍历文档每一行
            username,password = line.strip().split() #把每一行的字符串以空格分拆，并且赋值
            if Username == username and Password == password:#判断用户名和密码都正确
                print('成功登陆')
                userpass = 'T'
                break #成功校验后标记为T并且跳出当前循环到while判断标记为T然后跳出所有循环
if count >=3 and userpass == 'F':#精确判断次数和标记
    print("错误次数过多，账号被锁")
    with open(lock_file,'a+') as L:
        L.write('\n')
        L.write(Username)