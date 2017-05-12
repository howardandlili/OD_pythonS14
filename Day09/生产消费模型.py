#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
这是一个典型的生产消费者模型
一个是生产包子
几个吃包子
使用队列来控制
'''
import threading,queue,time

q = queue.Queue(maxsize=10)#建立队列实例

def producer(name):
    count = 1
    while True:
        q.put('包子%s'%count)
        print('%s生产了包子%s'%(name,count))
        count +=1
        time.sleep(1)
def Consumer(name):
    while True:
        print('%s拿到包子%s，吃了'%(name,q.get()))
        time.sleep(5)

p = threading.Thread(target=producer,args=('hy',))
c1 = threading.Thread(target=Consumer,args=('ll',))
c2 = threading.Thread(target=Consumer,args=('bb',))
c3 = threading.Thread(target=Consumer,args=('mm',))


p.start()
c1.start()
c2.start()
c3.start()