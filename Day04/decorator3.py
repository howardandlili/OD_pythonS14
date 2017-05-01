#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
装饰器
利用高级函数+嵌套函数把装饰器的功能实现出来
1.不能改变源代码和调用方式
2.附加功能
'''
import  time
def timmer(func):
    def jishi(*args,**kwargs):#当函数是有参数的时候就是等于附加功能是有参数
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print('run time is %s'%(stop_time-start_time))
    return jishi




@timmer#就是等于做了一步这个   func1=timmer(func1)  必须要在需要装饰器的函数上面加，每一个函数都需要加

def func1():
    time.sleep(2)
    print('in the func1')
@timmer
def func2(name): #当函数是有参数的时候就是等于附加功能是有参数
    time.sleep(1)
    print('in the func2',name)
#func1=timmer(func1)
# func1=jishi(func1)
func1()
func2('hy')

