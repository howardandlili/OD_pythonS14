#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import  paramiko

#private_key = paramiko.RSAKey.from_private_key_file('python_skey')
private_key = paramiko.RSAKey.from_private_key_file('id_rsa')#定义私钥

ssh = paramiko.SSHClient() #先建立一个实例

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())#允许连接不在列表中的主机

ssh.connect('124.172.245.95',60108,'root',pkey=private_key)#用密钥对来连接
#ssh.connect('124.172.245.95',60108,'root',password='intel@123')#用密钥对来连接


while True:
    command_inpt = input('你想要输入的命令：')

    stdin,stdout,stderr = ssh.exec_command(command_inpt)#发送命令返回了三个结果

    result_out = stdout.read()#获得返回的值这个是二进制的
    result_err = stderr.read()#获得返回的值这个是二进制的

    print(result_out.decode())
    print(result_err.decode())

ssh.close()

