#!/user/bin/env python

__author__ = 'Howie'
import  time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print('the func run time is %s'%(stop_time-start_time))
    return warpper

@timmer

def func1():
    time.sleep(3)
    print('this is func1')

func1()