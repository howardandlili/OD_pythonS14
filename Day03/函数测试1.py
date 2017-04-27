#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
def func1(x=2):
    '这是一个测试的函数，输入参数然后求平方值'
    y = x**10
    return y
a = func1(4)
b = func1()
print(a,b)
c = a + b
print(c)