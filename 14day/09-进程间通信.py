import os
import time
num = 1

p = os.fork()
if p == 0:
    time.sleep(3)
    if num == 2:
        print("我是子进程")
    else:
        print("呵呵")
else:
    num +=1
    print("我是父进程")


