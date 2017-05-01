#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
def fib(max):
    a,b = 0,1
    for n in range(max):
        print(b)
        a,b = b,a+b
    return 'Done'
#print(type(fib(10)))
#当我需要把他改成生成器的时候
def fib(max):
    a,b = 0,1
    for n in range(max):
    #    print(b)
        yield (b) #把原来的print改成yield就会变成生成器的了，
                  #他的作用就是当执行到这里的时候会中断生成器把需要输出的结果返回到函数体中去。
        a,b = b,a+b
    return 'Done'

#print(type(fib(10)))#输出就会变成<class 'generator'>

f = fib(10)
while True :
    try:
        x = f.__next__()
        print('f:',x)
    except StopIteration as e:
        print('出现错误代码',e.value)
        break


