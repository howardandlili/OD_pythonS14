#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
这是一个模拟CS是的类测试
'''
class Role(object):
    '首先定义建立一个角色模型'
    n = 123 #这个叫类变量，他可以不用实例化就直接被调用
    def __init__(self,name,role,weapon,live=100,money=15000):
        '开始构造函数主要是做在实例化时的一些类的初始化工作，我的理解是开始为每个对象开始赋值属于对象的变量'
        self.name = name #这个就是实例变量（也可以叫静态属性），他的作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.live = live
        self.money = money
    def buy_gun(self,gun):#这样的一个方法其实也是一个属性我们叫2他们做动态属性
        '开始定于类的方法'
        print('%s买了一支%s枪'%(self.name,gun))

    def get_shot(self):
        print('%s:啊我中枪了！！'%self.name)

    def shot(self):
        print('%s:我开枪了！！'%self.name)
#########################################
#上面就是一个类
print(Role.n) #在这里可以看见不需要实例化直接就可以调用类变量


#那么我要调用类来做一个对象（实例化）
r1 = Role('HY','police','B51')#这样把一个调用一个类完成一个对象的过程叫做实例化

r2 = Role('LiLi','恐怖分子','AK47')

#这样就完成了对象了r1,r2就是一个个对象他会把类的属性继承下来


#这样就是对象调用类的函数了
print(Role)#<class '__main__.Role'> 这里可以看见Role是一个类
print(r1.shot)#<bound method Role.shot of <__main__.Role object at 0x0000000001143E80>>
            #在这里可以看见这个对象在Role那里拿到了shot这个函数
print(r1) #<__main__.Role object at 0x0000000001173E80> 从这里可以看见他就是一个对象
            #是从Role这个类构造出来的




