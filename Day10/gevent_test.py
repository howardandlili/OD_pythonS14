#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import gevent

def task(pid):
    gevent.sleep(1)
    print('Task:%s done:'%pid)

def synchronous():
    for i in range(10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task,i) for  i in range(10)]
    gevent.joinall(threads)
# print('synchronous')
# synchronous()


print('asynchronous')
asynchronous()