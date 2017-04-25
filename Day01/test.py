#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
account_file = 'user.txt'
lock_file = 'account_lock.txt'
Username = 'wangwu'
Password = '789'
var = "This is a string"
varName = 'var'
s= locals()[varName]
s2=vars()[varName]





'''
def Province():
    print('省份有：',CN)
    menu = ('''
——————省份——————
1.%s    (1)
2.%s    (2)
3.返回    (B)
4.退出    (Q)
————————————————
    ''')% (CN[0],CN[1])
    print(menu)
def city():
    print('城市有：', CN)
    menu = ('''
——————城市——————
1.%s    (1)
2.%s    (2)
3.返回    (B)
4.退出    (Q)
————————————————
    ''') % (CN[0], CN[1])
    print(menu1)
def county():
    A = locals()[CN[NO]]
    print(A[NO])
def login():
    print('''
——————开始——————
1.省份。（1）
2.退出。（0）
————————————————
    ''')
login()
Province()
county()
'''