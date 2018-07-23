import os

pid = os.fork()
if pid == 0:
    print("老王")
else:
    print("老宋")

