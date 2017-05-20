#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import socket

#建立实例
sock = socket.socket()
#绑定IP端口
sock.bind(('localhost',8000))
#监听


sock.listen(5)
while True:
    conn,addr = sock.accept()
    res = conn.recv(1024)
    print(res)
    conn.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='gbk'))
    conn.send(bytes('你好，黄炎',encoding='utf-8'))
