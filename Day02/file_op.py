#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'


index = 0
#with open('yestherday','r+',encoding='utf-8') as data:
with open('yes2','r+',encoding='utf-8') as data:
	print(data.readline())
#	data.write('\n北京天安门太阳升！........')



'''
	print(data.readline(),data.tell())
	data.seek(10)
	print(data.readline(),data.tell())


	for line in data:
		index +=1
		if index <= 9 or index >=13:
			print('----不打印第%s行------'%index)
			continue
		print(index,line.strip())

'''


'''
	for index,line in enumerate(data.readlines()):
		if index <= 9 or index >=13:
			print('----不打印第%s行------'%index)
			continue
		print(index,line.strip())
'''
