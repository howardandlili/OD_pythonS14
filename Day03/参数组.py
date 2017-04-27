#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
def test1(x=1,*args,**kw):
    print(x)
    print(args)
    b = args[0]
    print(b)
    y = x + b
    print(kw)
    return y,'%s的年龄是%s'%(kw['name'],kw['age'])
a = test1(2,3,name='HY',age=30)
print(a)