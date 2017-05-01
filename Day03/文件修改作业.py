#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

import os,sys
__name__ == "__main__"


#定义输入字符是否是数字的函数
def numif(number_input):
    while not number_input.isdigit() : #判断是不是数字的字符串如果不是要求重新输入
        number_input = input('\033[31m %s不是数字请输入正确数字：\033[0m'%number_input)
    number = int(number_input) #把正确的输入结果赋值到变量
    return number         #返回变量（返回正确的数字）

# 查询显示并将文本生成程序需要的字典和列表
def show_list(file = 'haproxy'):
    backend_list = []
    backend_all_dict = {}
    backend_dict = {}
    server_list = []

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
    return  (backend_list,backend_all_dict)

#定义backend的界面并且返回backend列表和编号
def backend_show(backend_list):
    backend_show_dict = {}
    print(
'''---------------------------
欢迎来到haproxy文件配置平台
---------------------------
以下是backend的信息'''
    )
    for k,v in enumerate(backend_list,1):# 逐行读取backend信息并展示
        print(k,v)
        backend_show_dict[str(k)] = v
    return backend_show_dict # 返回backend和对应编号

# 展示backend下server内容
def server_show(backend_input,backend_all_dict):
    server_show_dict = {}
    server_list = backend_all_dict[backend_input]
    for k,v in enumerate(server_list,1):
        print(k,'name:%s server:%s weight:%s maxconn:%s' %(v['name'],v['server'],v['weight'],v['maxconn']))
    server_show_dict[k] = v
    return server_show_dict  # 返回编号对应的server字典


# 显示操作列表和编号，并返回操作编号
def action_list():
    print("-------------------------------------------------")
    print("操作清单如下：")
    print('''
    1.查询backend和server信息
    2.添加backend和server信息
    3.修改backend和server信息
    4.删除backend和server信息
    5.退出
    ''')
    print("-------------------------------------------------")
    action_num = numif(input("请输入需要操作的编号：（请输入数字）"))
    return action_num


#定义查询函数
def inquiry(inquiry_input):
    if inquiry_input in backend_show_dict:    # 编号输入分支,根据编号来找backend
        backend_input = backend_show_dict[inquiry_input]    # 输入编号得到backend
        print(backend_input, ":")
        server_show(backend_input, backend_all_dict)
    elif inquiry_input in backend_show_dict.values(): #名字输入，根据名字来找backend
        print(inquiry_input,':')
        server_show(inquiry_input,backend_show_dict)
    else:
        inquiry_input = input("输入错误，请重新输入：")# 校验异常输入

#定义添加函数
def add(add_input,file):
    print(backend_all_dict,add_input)
    backend_add = input("请输入新的backend的名字：")
    backend_all_dict[add_input] = input("请输入新的backend的内容：")
    pass

# 定义文档备份与回写功能
def backup(file):
    file_new = "%s_new"%file
    with open(file,'r') as f_read , open(file_new,'a+') as f_wirte:
        for line in f_read:





#########################
file = 'haproxy'
(backend_list, backend_all_dict) = show_list(file)# 调用show_list函数获取backend和server信息
backend_show_dict = backend_show(backend_list)
#backend_input = backend_show_dict['1']
#server_show(backend_input, backend_all_dict)
#backend_show_dict = backend_show(backend_list)    # 展示backend信息
action_num = action_list()    # 展示功能项，并输入操作编号
if action_num == 1:
    inquiry(input("请输入需要查询的backend编号或名称："))
if action_num == 2:
    add(input("请输入需要添加的现有backend编号或新backend名称："),file)