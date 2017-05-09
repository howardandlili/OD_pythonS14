#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import socket,os
#首先先创建一个实例
server = socket.socket()
#绑定IP和端口
server.bind(('localhost',9999))#里面要用一个元组的形式来写
#监听
server.listen()
#等待请求，把来的请求做成一个实例和标记地址
while True:#这里是为了可以接收下一个socket的请求
    print('等待请求')
    conn,addr = server.accept()# conn就是客户端连过来而在服务器端为其生成的一个连接实例
    print('接收到的地址是',addr)
    #把接收到的数据保存
    #如果想不停的接收和返回的话那么就不能断开socket，这里就来一个循环
    while True:
        print('开始接收数据')
        data = conn.recv(1024) #记得这里是实例在负责发送和接收也就是conn

        print('接收到数据%s',data)
        if not data:
            break

        #然后开始处理你的执行
        print('data:',data)
        data = os.popen(data.decode()).read()#这里如果客户端断开就会接收到空值那么这里最好做一个判断如果为空就跳出去
        #然后返回处理结果
        print(data)
        data = data.encode('utf-8')
        data_size = str(len(data)).encode()
        #先告诉对方data 的大小
        conn.send(data_size)
        if len(data) == 0:
            conn.send('您发送的数据有问题'.encode())
            continue
        #再发送data本身
        conn.send(data)
        print('返回',data_size)
    #那么如果发完了就关掉的话是不是不能接收下一个请求了啊？如果想的话我们就需要再建立一个实例也就是conn
#发完了就关闭这次socket
server.close()