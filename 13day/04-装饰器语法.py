def w1(fun):
    def inner():
        print("验证登录")
        fun()
    return inner

def test():
    print("---------支付------------")

#test()
test = w1(test)
test()

'''
t1 = w1(test1)
t1()
'''
