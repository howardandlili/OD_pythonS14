#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
producer
'''
import pika



#先建立一个实例
connection = pika.BlockingConnection(pika.ConnectionParameters(
                                        host='10.88.1.108'))
#建立通道
channel = connection.channel()

#建立queue

channel.queue_declare(queue='hello')#如果在这里加上durable=True消息不丢失（其实我觉得是队列不丢失）双方都要加上


#生产消息

channel.basic_publish(exchange='',#这个是绑定消息队列前的一个交换机（简单来说他控制了消息分配到那个队列）
                      routing_key='hello',#这个是绑定在那个关键字的队列
                      body='Hello,World!') #这个就是消息的本身
                    #properties=pika.BasicProperties(
                      #     delivery_mode=2, # make message persistent
                      # ))在这里加上这个就是消息队列都不丢失

connection.close() #关闭连接