#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import time


#定义消费者的行为过程
def consumer(name):
    print('%s想要吃包子了'%name)
#    baozi = yield #在这里需要把上面的执行返回并且中断等待，当有值传进来的时候继续执行下面的代码
    while True :
        baozi = yield #在这里需要把上面的执行返回并且中断等待，当有值传进来的时候继续执行下面的代码
        print('包子%s来了，被%s吃了'%(baozi,name))


#定义生产者的行为过程
def producer():
    c = consumer('柳黎')
    c1 = consumer('彬彬')
    c.__next__()
    c1.__next__()
    print('生产者开始做包子了')
    for i in range(10):
        time.sleep(1)
        c.send(i)
        c1.send(i)
producer()
