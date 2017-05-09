#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
ftp 服务端
步骤：
1.建立一个实例
2.绑定ip
3.监听
4.建立请求连接实例和标记
5.等待接收数据
6.处理
7.发送
8.关闭
'''
import  socket
server = socket.socket()
server.bind(('localhost',9999))
server.listen()
while True:
    print('等待新的连接')
    conn,addr = server.accept()
    print('接收到新的连接：',addr)
    while True:
        print('等待新的请求')
        client_data = conn.recv(1024)
        print('接收到数据',client_data)
        server_data = client_data.upper()
        server_data_size = str(len(server_data)).encode()
        conn.send(server_data_size)#发送长度
        print('开始发送数据：',server_data)
        if len(server_data) == 0 :
            print('看看有没有到这里')
            conn.send(b'Error')
            continue
        conn.send(server_data)
        print('已经发送了数据')



server.close()





