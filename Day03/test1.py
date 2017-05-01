#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
file = 'haproxy'
def backup(file):
    file_new = "%s_new"%file
    backend_name = input("请输入新的backend的名字：")
    server = input("请输入新的server的名字：")
    name = input("请输入新的name的名字：")
    weight = input("请输入新的weight的名字：")
    maxconn = input("请输入新的maxconn的名字：")

    with open(file,'r') as f_read , open(file_new,'a+') as f_wirte:
        for line in f_read:
            f_wirte.write(line)
        line ='''\nbackend %s
        server %s %s weight %s maxconn %s'''% (backend_name,server,name,weight,maxconn)
        f_wirte.write(line)

#server_dict = {'maxconn': '3000', 'weight': '20', 'server': '100.1.7.12', 'name': '100.1.7.12'}


# backend_list = ['www.oldboy.org', 'www.baidu.com']
# backend_show_dict = {'2': 'www.baidu.com', '1': 'www.oldboy.org'}
#
# backend_all_dict = {'www.hy.com':[{'maxconn': '3000',
#                                 'weight': '20',
#                                 'name': '100.1.7.12',
#                                 'server': '100.1.7.12'}]}

backup(file)