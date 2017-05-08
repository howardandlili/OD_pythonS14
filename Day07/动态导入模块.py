#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
反射的时候是通过字符串去映射内存中的对象


而动态导入就是知道目录结构导入
'''


#例如我已经知道了aa这个累是在lib下面
modname = 'lib.aa'
#我们都知道可以 直接
#from lib import aa
#那么现在我需要的是把获得的字符串用类似反射的方法把模块导入


lib = __import__(modname) #这样就等于把lib导入了
# print(lib)
# print(lib.aa)#<module 'lib.aa' from 'I:\\projeck\\OD_pythonS14\\Day07\\lib\\aa.py'>在这里你可以看可以调用aa了
# print(lib.aa.C)#<class 'lib.aa.C'>在这里你可以看见可以调用类了
#那么当C是字符串怎么办？OK 用反射
C  = getattr(lib.aa,'C')#<class 'lib.aa.C'>这样我们就可以get到了类了

obj = C()
print(obj.name) #这样就可以把获得的字符串反射成类的名字使用了



'''
但是不是很麻烦？？？是的~官方也不建议我们这样用
那么我们用官方建议的

'''
#首先把importlib导入
import  importlib


aa = importlib.import_module(modname)#这样的话我们就可以直接用上了aa这个模块了
print(aa)#<module 'lib.aa' from 'I:\\projeck\\OD_pythonS14\\Day07\\lib\\aa.py'>
print(aa.C().name)#这样就可以完成了当然如果C还是字符串的话还是要用反射

C = getattr(aa,'C')
print(C().name)