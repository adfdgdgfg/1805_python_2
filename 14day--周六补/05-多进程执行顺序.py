import os
import time

pid = os.fork()
if pid == 0:
    time.sleep(3)
    print("老王")
else:
    time.sleep(5)
    print("老宋")

