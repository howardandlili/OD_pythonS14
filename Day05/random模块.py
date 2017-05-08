#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
random 就是一个随机模块
'''
import random


srt = ''

for i in range(5):
    curent = random.randint(0,5)
    if curent == i:
        srt += str(random.randint(0,9))
    else:
        srt += chr(random.randint(65,90))
print(srt)


#     srt+=str(i)
# print(srt)