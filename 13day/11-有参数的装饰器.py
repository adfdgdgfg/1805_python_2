def w(type):
    def w1(fun):
        def inner():
            if type == 1:
                print("验证吃鸡账号")
            elif type == 2:
                print("验证王者账号")
            fun()
        return inner
    return w1

'''
def w2(fun):
    def inner():
        print("验证王者账号")
        fun()
    return inner
'''

@w(1)
def play1():
    print("我要玩吃鸡")

@w(2)
def play2():
    print("我要玩王者")

play1()
if __name__ == '__main__':
    main()
play2()
