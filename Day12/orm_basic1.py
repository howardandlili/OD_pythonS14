#!/user/bin/env python
__author__ = 'Howie'

'''
orm 是一种封装后的对象对应sql 的方法~
sqlalchemy就是其中最出色的一个模块
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("mysql+pymysql://python_user:python*-+@124.172.245.95/pydb",
                                    encoding='utf-8', echo=True)


Base = declarative_base() #生成orm基类

class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine) #创建表结构