#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
这里是表结构，
'''
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, DATE, Table, ForeignKey, create_engine


#创建连接实例
engine = create_engine("mysql+pymysql://python_user:python*-+@124.172.245.95/pydb?charset=utf8",encoding='utf-8')

#建立基类

Base = declarative_base()

#建立表类（映射关系）我们这里是需要三个表 Book（书的资料） Author（作者的资料） Book_to_Author（两个表的对应关系表）

#其中Book_to_Author表是不需要我们自己维护的所以不需要建类了直接建表
book_to_author = Table('book_to_author',Base.metadata,
                       Column('books_id',Integer,ForeignKey('books.id')),
                       Column('author_id',Integer,ForeignKey('authors.id')),
                       )


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=False)
    pub_date = Column(DATE,nullable=False)
    #这里还要加上外键对应查找的关系
    authors = relationship('Author', secondary=book_to_author, backref='books')
    # def __repr__(self):
    #     return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(16),nullable=False)
    def __repr__(self):
        return self.name

Base.metadata.create_all(engine)


#表结构已经OK 了
#开始插入内容