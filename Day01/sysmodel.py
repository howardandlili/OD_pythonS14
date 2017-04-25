#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

import sys,os
print(sys.argv)
#cmd_res = os.system('dir') #只执行不保存结果
#cmd_res = os.popen('dir').read() # 如果不加read 就只是作为一个内存对象而不是结果
#cmd_res = os.makedirs('testdir/test') .mkdir是当前创建目录，makedirs是多重目录

#print('--->',cmd_res)
a, b, c = 1, 3, 5
d = a if a > b else c
print(d)
