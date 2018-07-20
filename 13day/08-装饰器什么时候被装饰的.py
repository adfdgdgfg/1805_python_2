def w1(fun):
    print("哈哈")
    def inner():
        print("验证登录")
        fun()
    return inner


@w1#代码执行到这就已经装饰完毕了
def play():
    print("------------吃鸡---------------")


#play()
