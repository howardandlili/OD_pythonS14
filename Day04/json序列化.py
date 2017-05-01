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
# info = {
#     'name': 'howie',
#     'age': 30
# }
# with open('json_test.txt','w') as j:
#     print(json.dumps(info))
#     j.write(json.dumps(info))
# f = open('json_test.txt','w',encoding='utf-8')
# print(json.dumps(info))
#####################################
#以上就是用json的，但是很多时候json是无法完成一些比较复杂的处理的，但是我们有需要怎么办？
#pickle就出来了~用发和json一样的
import pickle

file = 'json_test.txt'

def func():
    print('this is a func')


info = {
    'name':'黄炎',
    'age':22,
    'func':func  #这里把json不能写入的函数内存地址也写进去了
}

with open(file,'wb') as p: #由于pickle 是传入二进制的所以要加上wb
    p.write(pickle.dumps(info))


