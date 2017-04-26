#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
def sed(old_str,new_str):
	import  sys

	old_str = sys.argv[1]
	new_str = sys.argv[2]

	with open('yes2','r',encoding='utf-8') as f,open('yes3','w',encoding='utf-8') as f1:
		for i in f:
			if 'old_str' in i:
				i = i.replace(old_str,new_str)
			f1.write(i)
sed('天安门..','我家的门..')