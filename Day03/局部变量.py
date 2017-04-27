#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

name = ['hy','ll','bb'] #当全局变量是列表，字典，类等这样的复杂数据类型时候。

def change_name():
	print('before:', name)
	name[0] = 'HY'      #在函数体内改了变量
	print('after:', name)#在函数中发现是改了

change_name()
print(name)             #在外面全局变量也是改了

'''
以上输出的结果：
before: ['hy', 'll', 'bb']
after: ['HY', 'll', 'bb']
['HY', 'll', 'bb']
'''





#############################################################
# def test1(name):
# #	global name #定义全局变量，如果不定义函数内的变量只作用于函数体内
# 	print('before',name)
# 	name = 'hh'
# 	print('after',name)
#
# name = 'Howie Huang'
#
#
# test1(name)
# print(name)

