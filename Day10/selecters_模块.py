#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import  selectors,socket
'''
selectors 是一个封装好的的多路径复用模块
有epoll就用
没有就用select
现在就用selectors 来做一个socket的服务器
'''

#和其他的一样先建立一个select实例
sel = selectors.DefaultSelector()

#建立新的连接
def accept(sock,mask):
    conn,addr = sock.accept()#创建连接实例
    print('accepted', conn, 'from', addr, mask)
    #上面是专门给新建连接用的，但是如果是建立好的连接传数据怎么办？OK 再监控，注册
    sel.register(conn,selectors.EVENT_READ,read)


def read(conn,mask):
    '这个是读取建立好的连接发过来的data'
    data = conn.recv(1024)
    print(data)
    if data:
        print('data',repr(data),'to',conn)
        conn.send(data)
    else:
        print('closing',conn,'data',data)
        sel.unregister(conn)#如果断开连接那么就把这个连接实例在注册表中删掉
        conn.close()




#开始做一个socket的实例，并且开始做连接过程
sock = socket.socket()
sock.bind(('localhost',9999))
sock.listen()
#做好了监听端口后就要接收创建连接实例，但是我想这个是多路复用
sock.setblocking(False)#开始非堵塞
sel.register(sock,selectors.EVENT_READ,accept)#注册连接实例(监控对象，方式，如果有事件发生调用的函数)

#OK 到了这里就完成了服务器的多路接收和发送了

#开始调用
while True:
    event = sel.select()#默认阻塞，有活动连接就返回活动的连接列表
    for key,mask in event:
        callback = key.data #accept
        callback(key.fileobj,mask)#key.fileobj=  文件句柄
