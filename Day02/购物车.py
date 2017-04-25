#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
需求：
	1.启动程序后，让用户输入工资，让后打印列表。
	2.允许用户根据标号购买商品。
	3.用户选择商品后，检测余额是否足够，够就直接扣款，不够就提醒。
	4.可随时退出，退出时，打印已购买商品和余额。
'''
product_list = [        #商品列表做成列表可以动态
	('Iphone', 5000),
	('Ipad', 2000),
	('Bike', 500),
	('Watch', 10000),
	('Coffee', 31),
	('MImu', 2400)
]
shopping_list = []
salary = input('输入您的工资：')
if salary.isdigit():    #判断输入的字符能不能转换整数
	salary = int(salary)#转换整数
	while True:
		for index, item in enumerate(product_list):#自动打印下标
			print(index,item)
		user_choise = input('选择您要购买的物品：')
		if user_choise.isdigit():
			user_choise = int(user_choise)
			if user_choise < len(product_list) and user_choise >=0:#判断输入的数字是不是在列表长度之内。
				p_item = product_list[user_choise]  #将选中的商品取出
				if p_item[1] <= salary: #判断是不是买得起，如果买得起
					salary -=p_item[1]
					print('您已购买商品【%s】,余额为\033[31;1m%s\033[0m' %(p_item[0],salary))
					shopping_list.append(p_item)
				else:
					print('你的余额为%s,\033[33;1m%s价格为%s,余额不足\033[0m'%(salary,p_item[0],p_item[1]))
			else:
				print('请输入正确数值0~%s'%(len(product_list)-1))
		elif user_choise == 'q':

			print('谢谢您的购买，您购买的商品是')
			for index,item in enumerate(shopping_list):
				print(index,item)
			print('您的余额是',salary)
			exit()
else:
	print('请输入正确的金钱数')
#记得主要是分清楚循环的等级关系很重要












