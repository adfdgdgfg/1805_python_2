def w1(fun):
    def inner(*args,**kwargs):
        print("验证登录")
        return fun(*args,**kwargs)
    return inner


@w1
def play(a,b):
    print("------------%s-----%s----------"%(a,b))
    return "hehe"

ret = play("1","2")
print(ret)

@w1
def play1():
    print("哈哈哈")
play1()


@w1
def play2(a):
    print("哈哈哈2%s"%a)
play2("嘎嘎")

@w1
def play3():
    return "hahah3"

ret = play3()
print(ret)
