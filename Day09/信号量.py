#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import time,threading

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('run the thread: %s'% n)
    semaphore.release()
semaphore = threading.BoundedSemaphore(5)
for i in range(10):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.start()


while threading.active_count() != 1:
    pass
#    print (threading.active_count())
else:
    print('做完了',threading.current_thread())