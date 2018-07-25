from multiprocessing import Pool
import time
import os

def work():#子进程要执行的逻辑
    for i in range(3):
        time.sleep(1)
        print("我是老王pid=%d"%os.getpid())


p = Pool(3)#最大装3个进程


for i in range(6):
    p.apply_async(work)#非阻塞添加进程
    #p.apply(work)#阻塞添加进程
p.close()#关闭池子
p.join()#开启子进程
    


