#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

account_file = 'user.txt'
lock_file = 'account_lock.txt'
username = 'll'
password = '789'
userpass = 'F'
count = 0

while userpass == 'F' and count <3: #当检验用户名不通过并且检验次数小于3次的时候才做检验
    with open(lock_file,'r') as l:  #打开锁用户文件
        for line in l.readlines():  #遍历整个文件的每一行
            if username == line.strip(): #去掉空格和换行
                print('L')
                continue
            else:
                with open(account_file,'r') as l:
                    for line in l.readlines():
                        Username,Password = line.strip().split()
                        if Username == username and Password == password:
                            print('OK')
                            userpass = 'T'
                            break
                    else:
                        print('NO')
                        count +=1
if count >= 3:
    print('3ci')



