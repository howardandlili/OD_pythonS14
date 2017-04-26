#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
readme:
这个是一个三级菜单，通过输入对应的名字可以进到下一层，在任何一层可以退出。
'''
#首先
data = {
    '广东省':{
        '广州':['白云','越秀'],
        '茂名':['高州','电白']
    },
    '山东省':{
        '山东市1':['山东县1','山东县11'],
        '山东市2':['山东县2','山东县22']
    },
    '广西省':{
        '广西市1':['广西县1','广西县11'],
        '广西市2':['广西县2','广西县22']
    }
}
while True:
    for i in data :
        print(i)
    choice1 = input('要查看的省：')
    if choice1 in data:
        while True:
            for i2 in data[choice1]:
                print(i2)
            choice2 = input('要查看的市：')
            if choice2 in data[choice1]:
                for i3 in data[choice1][choice2]:
                    print(i3)
                choice3 = input('已经最后一层了，按’b‘返回或者按’q‘退出 ：')
                if choice3 == 'b':
                    pass
                if choice3 == 'q':
                    exit()
            if choice2 == 'b':
                break
            if choice2 == 'q':
                exit()
    if choice1 == 'q':
        exit()