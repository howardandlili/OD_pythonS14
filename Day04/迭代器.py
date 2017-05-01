#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
迭代器：
首先可以循环的数据类型是
（list,tuple,dict,str,set）
generator,包括生成器和带yield的generator的function
这些都是可以直接作用循环的循环体也可以看作是对象，而这些对象被称为可迭代的对象Iterable
可以用isinstance()来判断是不是iterable

生成器是可以被next()函数不停调用并且返回下一个值，直到最后无法返回下一个值的时候出现异常Stopiteration
而！！！可以被next()调用并且返回下一个值的对象叫做迭代器：Iterator！！！
可以用isinstance()老判断是不是Iterator对象

我的理解（注意不一定正确）
Iterable 其实就是一个循环体
而
Iterator 其实就是一个函数，他是可以可以被netx()调用并且可以返回值的
那么Iterable是不是可以变成Iterator呢？
是可以的


'''
a = [1,2,3,4] #a是一个list，也可以说是一个Iterable
b = iter(a)#这样就可以把他变成一个Itertor了
#那么b就是可以被next()调用了
print(next(b))
print(next(b))
print(next(b))

'''
list,dict,set,tuple 等等为什么就不能是Iterator呢？
其实最简单的理解方法就是一个[]就是一个固定的值已经确定存在了，而Iterator却是要被调用的时候才有值返回的
'''


