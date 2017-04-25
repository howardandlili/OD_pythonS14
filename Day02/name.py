#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
names = ['ZhangSan', 'LiSi', 'WangWu',['lili','dddd'], 'ZhaoLiu','DAda']
#A = names[-2:] #如果想取倒数几个数需要吧最后一个省略
A = names[:3] #如果想取第一个开始到第几个数可以把索引值省略
print(A)
names.append('Lili')#追加
print(names)
name2 = names.copy()
print('浅拷贝后：',name2)
names[2] = '王五'
names[3][0] = 'LILI'
print('原列表：',names)
print('浅拷贝后再修改原列表的子列表：的',name2)

#如果想要完全复制的话要导入一个模块
import copy
name2 = copy.copy(names)
print('原列表：',names)
print('完全复制后：', name2)



#names.pop(1) #删除第二个
#del names[1]  #和上面的差不多一样的
names.remove('LiSi') #匹配删除
print('删除',names)
names.insert(1,'DAda')#中间插入数值问索引值
print(names)
names[2] = 'xiugai' # 改就是等再赋值一次
print(names)
print('查询值在索引位置：',names.index('DAda'))
print('统计名字次数：',names.count('DAda'))
names.reverse()
names2 = ['66','3','6','8','1','5']
names.extend(names2)
print('扩张：',names)

#names.sort()
#print('排序：',names)




names.clear()
print(names)




