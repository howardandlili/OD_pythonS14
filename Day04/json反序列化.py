#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
把字典的信息想要写到文本中直接写是不行的
但是我们可以吧字典写成字符串就可以了
那么我们怎么把字典写成字符串呢？
JSON就可以了
'''

# import json
#
# with open('json_test.txt') as j:
#     info = json.loads(j.read())
# print(info['name'])
######################################33
#用pikle做反序列化
import pickle

file = 'json_test.txt'

def func():
    print('this is a func')

with open(file,'rb') as p:
    info = pickle.loads(p.read())
print(info['func'])