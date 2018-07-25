from multiprocessing import Pool
import time
import os

def test():#子进程
    #print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(10):
        print("做饭中")
        time.sleep(1)
    return "做好了"

def test2(args):
    #print("---callback func--pid=%d"%os.getpid())
    print(args+"快来吃饭吧 孩子")

pool = Pool(3)
pool.apply_async(func=test,callback=test2)#非阻塞添加

for i in range(100000000):
	time.sleep(1)
	print("我在写作业")

print("----主进程-pid=%d----"%os.getpid())