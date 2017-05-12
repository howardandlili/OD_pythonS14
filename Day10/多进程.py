#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
多进程的语法和多线程差不多的
'''

import multiprocessing,time,threading

def run(name):
    print(name)
    t = threading.Thread(target=pid)
    t.start()
    time.sleep(1)

def pid():
    print(threading.get_ident())


if __name__ == '__main__':
    for i in range(10):
       p = multiprocessing.Process(target=run,args=('%s'%i,))
       p.start()
