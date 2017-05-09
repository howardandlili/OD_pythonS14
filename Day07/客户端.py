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
    #接着就可以收了,但是这时候是不是应该想如果一次接收不完是不是应该继续接收？是的
    print('开始接收数据的大小')
    #第一次是接收到data的大小
    data_size = int(client.recv(1024).decode())
    print('数据文件大小为',data_size)

    #然后就开始判断什么时候才可以把data都收完
    recv_data = ''
    data_recv_all_size = -1
    while data_recv_all_size < data_size :
        #开始接收数据
        print('开始接收数据')
        recv_data = client.recv(1024)
        #判断数据大小
        print('判断数据大小')
        data_recv_size = len(recv_data)
        data_recv_all_size += data_recv_size

        print('接收到的数据为：',recv_data.decode())
    print('已经接收到的文件大小为:', data_recv_all_size)
print('结束会话')
