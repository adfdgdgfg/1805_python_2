def w1(fun):
    def inner(*args,**kwargs):
        print("验证登录")
        fun(*args,**kwargs)
    return inner


@w1
def play(a,b):
    print("------------%s-----%s----------"%(a,b))


play("1","2")
