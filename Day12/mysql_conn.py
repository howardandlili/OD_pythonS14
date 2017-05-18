#!/user/bin/env python
__author__ = 'Howie'


import pymysql

#创建实例

conn = pymysql.connect(host='124.172.245.95',port=3306,user='python_user',password='python*-+',database='pydb')

#创建游标（也就是去到shell那里）

cursor = conn.cursor()

#开始执行sql，并且返回受影响行数

effect = cursor.execute('select * from stu')

data = cursor.fetchone()
print('data-->',data[1])

print(effect)

conn.close()