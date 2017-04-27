#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
1、查
    输入：www.oldboy.org
    获取当前backend下的所有记录

2、新建
    输入：
        arg = {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }

3、删除
    输入：
        arg = {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }
'''
import linecache

backend = []
server = []


def find():
	with open('haproxy','r') as f1,open('haproxy.bk','a+') as f2:
		count = 0
		for line in f1:
			count +=1
			line =line.strip()

			if line.startswith('backend'):
				line =line.strip().split()
				backend.append(line[1])
				print(backend)
			elif line.startswith('server'):
				line =line.strip().split()
				server.append(line[1])
				print(server)
				return (backend)
find()
print(find())
	#			f2.write('%s\n'%line)
			# elif line.startswith('server'):
			# 	server_line=print(line)
	#			f2.write('%s\n'%line)



