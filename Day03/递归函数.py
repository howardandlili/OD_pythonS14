#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
def cale(n):
	print(n)
	if int(n/2) >0:
		return cale(int(n/2))
	print('--->',n)
cale(10)