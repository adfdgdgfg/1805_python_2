from threading import Thread,Lock
import time
num = 0
def work1():
    global num
    #mutex.acquire(True)#阻塞上锁
    for i in range(1000000):
        mutex.acquire(True)
        num += 1
        mutex.release()#释放锁
    #mutex.release()
    print("线程一%d"%num)


def work2():
    global num #在函数内部修改全局变量要加global声明
    #mutex.acquire(True)#阻塞
    for i in range(1000000):
        mutex.acquire(True)
        num +=1
        mutex.release()
    #mutex.release()
    print("线程二%d"%num)

mutex = Lock()#创建一把锁

t = Thread(target=work1)#创建一个线程
t1 = Thread(target=work2)#创建一个线程
t.start()#创建启动
#time.sleep(10)
t1.start()#线程启动
