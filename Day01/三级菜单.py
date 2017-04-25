#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
作业要求：
三级菜单要有返回键
可依次进入各个菜单
'''
##########################
'''
readme：
这是一个中国的三级菜单，可以依次省，市，县三级。
可以在任何一级返回上一级。
'''
GZ = ['BY', 'YX']
MM = ['ggz', 'db']
SD1 = ['SD11', 'SD12']
SD2 = ['SD21', 'SD22']
GD = ['GZ', 'MM']
SD = ['SD1', 'SD2']
CN = ['SD', 'GD']
NO = 0
def Choose():
    NO = input('请输入您的序号：')
    return NO
def province():
    print('''
    你要找的省份为
    ''',
    CN[0], CN[1]
    )
    Choose()
def menu():
    print('''
    你要的选择
    1.查看省份
    2.退出
    ''')
while NO != 'Q':
    print('''
        你要的选择
        1.查看省份
        2.退出
        ''')
    NO = int(input('请输入您的序号：'))
    print(NO)
    if NO == 1:
        CN = 'SD'
        A = ('''
            你要找的省份是：{city1},{city2}
            你要选择的是
            1. {city1}
            2. {city2}
            3.返回
            4.退出
            ''').format(city1=CN[(NO-1)], city2=CN[NO])
        print(A)
        NO = int(input('请输入您的序号：'))
        if NO == 0:
            break
        else :
            A = ('''
            你要找的城市是：{city1},{city2}
            你要选择的是
            1. {city1}
            2. {city2}
            3.返回
            4.退出
            ''').format(city1=CN[(NO-1)], city2=CN[NO])
            print(A)
            NO = int(input('请输入您的序号：'))
