#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

import os,sys
__name__ == "__main__"

def numif(number_input): #定义输入字符是否是数字的函数
    while not number_input.isdigit() : #判断是不是数字的字符串如果不是要求重新输入
        number_input = input('\033[31m %s不是数字请输入正确数字：\033[0m'%number_input)
    number = number_input #把正确的输入结果赋值到变量
    return number         #返回变量（返回正确的数字）


def show_list():    # 查询显示并将文本生成程序需要的字典和列表
    backend_list = []
    backend_all_dict = {}
    backend_dict = {}
    server_list = []

    file = 'haproxy'
    with open(file, 'r') as f:  # 读取haproxy文件
        for line in f:          #每一行读取文件
            line = line.strip() #去掉头尾的空格和换行符
            if line.startswith('backend'):#判断以关键字开头的行
                backend_name = line.split()[1]#把行用空格分割成列表，并且把所需要的值取出来
                backend_list.append(backend_name)#把取到的值追加成一个列表
                server_list = []            #清空当前列表等下一行来的时候可以干净写入

            elif line.startswith('server'):#这一行是比较多的KEY所有需要做成字典
                backend_dict['name'] = line.split()[1]#按照KEY来赋值做成字典
                backend_dict['server'] = line.split()[2]
                backend_dict['weight'] = line.split()[4]
                backend_dict['maxconn'] = line.split()[6]
                server_list.append(backend_dict.copy())#需要用浅复制内存地址，避免覆盖掉
                backend_all_dict[backend_name] = server_list# 将server信息对应backend存到字典中
    return  (backend_all_dict, backend_list)


print('''
欢迎来到haproxy修改系统
backend列表信息如下''')
while True:
    for index,domain in enumerate(show_list()[1]):
        print(index,domain)
    number = int(numif(input('请输入您要查询的号码：')))
    backend_all = show_list()[0] #把信息取出来用于找到对应的server信息
    backend_list = show_list()[1]#把名字取出来用于匹配字典
    if number > len(backend_list):
        print('太大了')
        continue
    print(backend_all[backend_list[number]])




