#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
红灯停，路灯走
使用事情的set，clear，wait来控制
'''

import threading,time
event = threading.Event()

def lingter():
    count = 1
    while True:
        if count >=0 and count<10:
            event.set()
            print('绿灯',(10 - count))
        elif count>=10 and count<15:
            event.clear()
            print('红灯',15-count)
        else:
            count = 0
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print('%s开车中。。。。。。'%name)
            time.sleep(1)
        else:
            print('%s停车' % name)
            event.wait()
            print('%s等到绿灯亮了继续走。。。。。。' % name)



light = threading.Thread(target=lingter,)
light.start()
car = threading.Thread(target=car,args=('宝骏560',))
car.start()

