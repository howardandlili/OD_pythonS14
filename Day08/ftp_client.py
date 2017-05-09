#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
FTP客户端:
1.建立实例
2.开始连接
3.开始发送
4.开始接收
'''
import socket


client = socket.socket()
client.connect(('localhost',9999))
while True:
    client_data_str = input('>>>')
    client_data_b = client_data_str.encode()
    client.send(client_data_b)
    server_data_sizec_b = client.recv(1024)#接收长度
    print('长度为：',server_data_sizec_b)
#    server_data_sizec_int = int(server_data_sizec_b.deconde())
#    if server_data_sizec_int :
    print('等待服务端的发送')
#    server_data_b = client.recv(1024)
#    server_data_str = server_data_b.decode()
#    print('recv>>',server_data_str)
