#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

import time

mag = ''

def log_add():
    time_format = '%Y-%m-%d %x'
    time_current = time.strftime(time_format)
    with open('log','a+',encoding='utf-8') as f:
        f.write('%s追加一行,___%s\n'%(time_current,mag))

mag = 'test1'

def test1():
    print('this is test1')
    log_add()


def test2():
    print('this is test2')
    log_add()


def test3():
    print('this is test3')
    log_add()
test1()
test2()
test3()
