#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
连接数据库接口
'''
from Day12 import orm_m2m_system
from sqlalchemy.orm import sessionmaker


#创建会话

Session_class = sessionmaker(bind=orm_m2m_system.engine)
session = Session_class()
'''
#定于data

b1 = orm_m2m_system.Book(name='跟我学python',pub_date='2016-03-01')
b2 = orm_m2m_system.Book(name='跟我学Linux',pub_date='2016-05-01')
b3 = orm_m2m_system.Book(name='跟我学nginx',pub_date='2014-06-01')

a1 = orm_m2m_system.Author(name='黄炎')
a2 = orm_m2m_system.Author(name='柳黎')
a3 = orm_m2m_system.Author(name='彬彬')



#开始把两个字段

b1.authors = [a1, a2]
b2.authors = [a1, a2, a3]
b3.authors = [a2, a3]

#开始交给会话执行

session.add_all([b1, b2, b3, a1, a2, a3])
'''
#查询

author_obj = session.query(orm_m2m_system.Author).filter(orm_m2m_system.Author.name=='彬彬').first()
print(author_obj.books[0].name,author_obj.books[0].pub_date)
books_obj = session.query(orm_m2m_system.Book).filter(orm_m2m_system.Book.id==3).first()
print(books_obj.authors)
#提交任务
session.commit()