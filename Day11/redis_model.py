#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
缓存系统
就是两个进程直接通过一个中间的内存缓存来达到一个高速的资源共享
redis就是比较火的一个
'''
import redis

# r = redis.Redis('10.88.1.82',6379)
# r.set('name','Howie')
# print(r.get('name'))

'''
2、连接池

redis-py使用connection pool来管理对一个redis server的所有连接，
避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。
可以直接建立一个连接池，然后作为参数Redis，
这样就可以实现多个Redis实例共享一个连接池

'''
pool = redis.ConnectionPool(host='10.88.1.82',)
r = redis.Redis(connection_pool=pool)
r.set('name','ly')
print(r.get('name'))
print(r.get('name').decode('utf-8'))