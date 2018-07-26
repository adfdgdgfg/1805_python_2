from socket import *

#创建一个tcp的套接字
s = socket(AF_INET,SOCK_STREAM)

#这个是链接服务器，做了一件三次握手
s.connect(("172.20.10.2",6688))

while True:
	cotent = input("请输入内容")
	s.send(cotent.encode("gb2312"))
	msg = s.recv(1024)
	print(msg.decode("gb2312"))
