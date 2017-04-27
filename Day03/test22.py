#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

school = "Oldboy edu."


def change_name(name):
    global school
    school = "Mage Linux"
    print("before change",name,school)
    name ="Alex li" #这个函数就是这个变量的作用域
    age =23
    print("after change",name)



print("school:",school)

name = "alex"
change_name(name)
print(name)

print("age",age)