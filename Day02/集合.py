#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
list_1 = [1,5,8,6,2,4,3,2,5,1,1,6]
list_2 = set([1,5,5,1,1,6,44,11,22])
list_1 = set(list_1)
print(list_1,list_2)
print('交集还可以用&来做：',list_1.intersection(list_2))
print('交集还可以用&来做：',list_1 &list_2)
print('并集：',list_1.union(list_2))
print('并集还可以用|来做：',list_1|list_2)
print('差集：',list_1.difference(list_2))#1有但是2没有的
print('差集还可以用-来做：',list_1-list_2)#1有但是2没有的
print('对称差集：',list_1.symmetric_difference(list_2))#除了交集以外的集合
print('对称差集还可以用^来做：',list_1^list_2)#除了交集以外的集合

list_3 = list_1.union(list_2)
print('子集：',list_1.issubset(list_2),list_1.issubset(list_3))#判断是不是子集
print('父集：',list_3.issuperset(list_1))
list_4 = set([333,5555,66666])
print('判断是不是没有交集如果没有就为True：',list_1.isdisjoint(list_4))
list_4.add(44444)
list_4.update([11111,2222,66,333])
list_4.remove(333)
print(list_4)