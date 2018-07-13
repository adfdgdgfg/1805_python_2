#coding=utf-8
'''
可能会出现异常代码要加上捕获异常
'''
try:
    #print(test)
    #open("laowang.txt","r")
    11/0
    print("老王")
except (NameError,FileNotFoundError):
    print("捕获知道的错误类型")
except Exception as ret:
    print(ret)
    print("捕获不知道的错误类型")
else:#当做程序没有错误的时候会走
    print("没有错误会执行")
finally:
    print("不管有错没错都执行")
