#!/user/bin/env python
# -*- coding:utf-8 -*-
name = input('name:')
age = input('age:')
job = input('job:')
salary = input('salary:')
info1 = '''
----------INFO1 %s----------
name = %s
age = %s
job = %s
salary = %s
''' % (name, name, age, job, salary)
print(info1)
info2 = '''
----------INFO2 {name}----------
name = {name}
age = {age}
job = {job}
salary = {salary}
''' .format(name=name, age=age, job=job, salary=salary)
print(info2)