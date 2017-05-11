#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import threading,time

def run(n):
    print('talk',n)
    time.sleep(2)
    print('thread done....',n,threading.current_thread())
# 用循环的方法
t_obj = []
time_start = time.time()
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.setDaemon(True)
    t.start()


time.sleep(2)
print('all threading is rund...',threading.current_thread(),threading.active_count())
print('cost:',time.time()-time_start)

