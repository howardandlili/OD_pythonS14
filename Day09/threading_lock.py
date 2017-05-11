#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import threading,time

coun = 0

def run(n):
    global coun
    coun += 1
    time.sleep(2)
# 用循环的方法
t_obj = []
lock = threading.Lock()

time_start = time.time()
for i in range(50):

    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.start()

print('coun:',coun)


