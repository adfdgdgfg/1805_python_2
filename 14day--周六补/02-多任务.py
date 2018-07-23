import time
def sing():
    for i in range(3):
        time.sleep(1)
        print("sing--------")


def dance():
    for i in range(3):
        time.sleep(1)
        print("dance-------")


while True:
    sing()
    dance()
    
