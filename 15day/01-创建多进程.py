import os
import time

p = os.fork()
if p == 0:
    print("进程%d 父进程的%d"%(os.getpid(),os.getppid()))
    time.sleep(3)
    print("子进程")
else:
    print("父进程")

