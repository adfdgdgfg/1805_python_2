import os
import time
num = 1

p = os.fork()
if p == 0:
    time.sleep(1)
    print(num)
else:
    num +=1
    print(num)
