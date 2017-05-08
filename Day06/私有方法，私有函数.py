#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
class Role(object):
    def __init__(self,name,role,weapen,live=100,money=1500):
        self.name = name
        self.role = role
        self.weapen = weapen
        self.__live = live#这样定于属性就是私有属性，他是不允许外部调用的，内部可以调用
        self.money = money
    def buy_gun(self,gun):
        print('%s买%s枪了'%(self.name,gun))

    def get_shot(self):
        self.__live -= 50 #这样就可以被内部调用
        print('%s中枪了,剩余%s生命'%(self.name,self.__live))

    def _shot(self):#这样就是私有方法也是不能被外部调用的
        print('shot.........')

r1 = Role('HY','恐怖分子','ak47')
r1.buy_gun('AK47')
r1.get_shot()
