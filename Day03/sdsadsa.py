#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'


backend_list = []
backend_all_dict = {}
backend_dict = {}
server_list = []

file = 'haproxy'
with open(file,'r') as f:    # 读取haproxy文件
    for line in f:

        line = line.strip()
        if line.startswith('backend'):
            backend_name = line.split()[1]
            backend_list.append(backend_name)
            server_list = []

        elif line.startswith('server'):
            backend_dict['name'] = line.split()[1]
            backend_dict['server'] = line.split()[2]
            backend_dict['weight'] = line.split()[4]
            backend_dict['maxconn'] = line.split()[6]
            server_list.append(backend_dict.copy())
            backend_all_dict[backend_name] = server_list

