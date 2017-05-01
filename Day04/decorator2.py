#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
嵌套函数：
就是在定义一个函数的函数体内再定义一个函数
由于函数即变量
所以在函数体内的定义的函数是只作用于函数体内
'''
# def foo():
#     print('in the foo')
#     def bar():
#         print('in the bar')
#     bar()
#
# foo()
x = 0
def grandpa():
    #x = 1
    def dad():
        x = 2
        def son():
            x=3
            print(x)
        son()
    dad()
grandpa()



