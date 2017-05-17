#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
consumer
消费者，也就是取出消息的一方
'''
import pika

#先建立实例


connection = pika.BlockingConnection(pika.ConnectionParameters(
                                            host='124.172.245.95',
                                                               ))

#建立通道
channel = connection.channel()

#建立要绑定的queue
channel.queue_declare(queue='hello')#如果在这里加上durable=True消息不丢失（其实我觉得是队列不丢失）双方都要加上

def calback(ch,method,properties, body):
    '定义回调方法'
    print(" [x] Received: %s" % body.decode())


#开始消费消息
channel.basic_consume(calback,#这里定于了消费消息的时候要调用的方法
                      queue='hello',#这里是队列
                      no_ack=True) #这里是不是要回应对方
                        #no-ack ＝ False，如果消费者遇到情况
                        # (its channel is closed, connection is closed, or TCP connection is lost)挂掉了，
                        #  那么，RabbitMQ会重新将该任务添加到队列中。

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming() #消费一旦开启就会堵塞