import os

pid = os.fork()
if pid == 0:
    print("老王")
    print("我是子进程进程号是%d 我的父亲进程是%d"%(os.getpid(),os.getppid()))
else:
    print("我是父进程我的进程号是%d 我的父亲的进程号是%d"%(os.getpid(),os.getppid()))
    print("老宋")

