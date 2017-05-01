#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''

'''
#先要认识列表生成器
a = [x*2 for x in range(10)]
#他其实就是等于
# b = []
# for x in range(10):
#     b.append(x *2)
# print(a,'\n',b)
#把[]改成()就是生成器
c = (x*2 for x in range(10))
print(c)#输出结果就是<generator object <genexpr> at 0x0000000000D17BA0>
#他其实就是一个等待调用的函数~本身没有结果等待调用的时候才返回结果，用__next__()来调用

print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
