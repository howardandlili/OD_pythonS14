#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import threading,time

def run(n):
    print('talk',n)
    time.sleep(2)
# 用循环的方法
t_obj = []
time_start = time.time()
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.start()
    t_obj.append(t)

for t_res in t_obj:
    t_res.join()
print(t_obj)
print('cost:',time.time()-time_start)

# th1 = threading.Thread(target=run,args=('t1',))
# th2 = threading.Thread(target=run,args=('t2',))
# th1.start()
# th2.start()

#用类的方式

# class Mythead(threading.Thread):
#     def __init__(self,n):
#         super(Mythead,self).__init__()
#         self.n = n
#     def run(self):
#         print('task',self.n)
#         time.sleep(3)
# t1 = Mythead('t1')
# t2 = Mythead('t2')
#
# t1.start()
# t2.start()