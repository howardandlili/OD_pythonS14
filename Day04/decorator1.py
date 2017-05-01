#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
# def bar():
#     print('in the bar:')
# def foo():
#     print('in the foo:')
#     bar()



# def foo():
#     print('in the foo:')
#     bar() #当函数体重要调用另外的函数，而且被调用的函数在后面被定义的时候也是可以的
# def bar():
#     print('in the bar:')
#
#
# foo()
# def bar():
#     print('in the bar')
# def foo(func):
#     print(func)
# foo(bar)
__author__ = "Alex Li"

import time
def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return warpper

@timmer
def func1():
    time.sleep(3)
    print('in the func1')

func1()