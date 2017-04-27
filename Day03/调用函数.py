#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
def test(x):
    y = x+1
    return y
a = test(1)

print(a)


def log(x=0):
    mag = x**10
    return mag

def log1(x=0):
    mag = log(x) + 1
    return mag


print(log1(2))