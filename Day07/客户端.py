#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
#先要导入socket模块
import socket


#首先要建立一个socket的实例
client = socket.socket()#默认就是 ipv4 tcp/ip
#然后就开始了连接
client.connect(('localhost',9999))
#接着开始发送，可以连续发送然后再接收的
count = 1
for i in range(30):
    data = input('输入你要的：')
    client.send(data.encode('utf-8'))
    #接着就可以收了
    data = client.recv(1024)
    print('recv:',data.decode())
print('结束会话')
