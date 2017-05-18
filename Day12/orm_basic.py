#!/user/bin/env python
__author__ = 'Howie'

'''
orm 是一种封装后的对象对应sql 的方法~
sqlalchemy就是其中最出色的一个模块
'''
import  sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

#首先我们要建立一个连接
#看见后面?charset=utf8了吗？这个是中文的关键~！谁叫我们是中国人呢！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

engine = create_engine("mysql+pymysql://python_user:python*-+@124.172.245.95/pydb?charset=utf8",encoding='utf-8')


#生成orm基类
Base = declarative_base()

#创建表结构的类

class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    password = Column(String(64))
    #如果想要返回是看得懂的结果就要这里再定于一个方法
    def __repr__(self):
        return '<User(name:%s, Password:%s)>'%(self.name,self.password)

#实例化~也就是创建表

Base.metadata.create_all(engine)


#表结构OK 了就开始插入数据了



Session_class = sessionmaker(bind=engine) #这里是创建一个和数据库连接的会话，记得这里是类！还要绑定在哪个连接上面
#生成会话实例
Session = Session_class()
##############插入数据######################


#创建你要的data对象

# user_obj = User(name='柳黎',password='123456')


#此时还没创建对象呢，不信你打印一下id发现还是None,也就是说还没有插入数据
# print(user_obj.name,user_obj.id)

#把要操作的data对象加入到会话中，统一创建

# Session.add(user_obj)

#上面也只是加入但是还不会操作
# print(user_obj.name,user_obj.id)

####################查数据########################
#查数据
# data = Session.query(User).filter(这里是加上过滤的条件可以多个filter).all()
# print(data)

####################修改数据########################
#那么从上面你可以知道自己的数据是一个对象了，那么修改就是直接赋值就OK了
# data = Session.query(User).filter(User.id==2).first()
# data.name = '彬彬'
# print(data)

####################删数据########################



#真正要操作的时候到了提交！到这里就会操作了（记得sqlalchemy是自动事务的）




Session.commit()

