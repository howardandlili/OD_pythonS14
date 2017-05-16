#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

import socket
'''
socket 客户端

'''

sock = socket.socket()
sock.connect(('localhost',9999))

while True:
    data = input('>>>>')
    sock.send(data.encode())
    res = sock.recv(1024)
    print('res:',res)
sock.close()