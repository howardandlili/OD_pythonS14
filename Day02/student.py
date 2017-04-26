#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
stu1 = {'name':'张三','class':'1','report':51}
stu2 = {'name':'李四','class':'1','report':61}
stu3 = {'name':'王五','class':'2','report':52}
stu4 = {'name':'赵六','class':'2','report':62}
roster = [stu1,stu2,stu3,stu4]

roster[2]['name'] = '王留'
print(roster)
print(stu3)