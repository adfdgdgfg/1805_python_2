from socket import *

#服务器
#AF_INET ipv4

s = socket(AF_INET,SOCK_STREAM)

s.bind(("",8889))
print("------11111-------")
s.listen(5)#监听最大客服端链接数
print("--------2222-------")
client,address =  s.accept()#等着接电话
print("---------3333----------")
msg = client.recv(1024)#接受消息

print(msg.decode("gb2312"))

client.send("哈哈".encode("gb2312"))

client.close()#关闭

s.close()#关闭
