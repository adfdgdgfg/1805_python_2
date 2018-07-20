class Test():
    def __init__(self,fun):
        #print("init")
        self.fun = fun

    def __call__(self):
        print("验证登录")
        self.fun()
        


'''
play = Test(xxx)
print(play())
'''


@Test#play = Test(play)
def play():
    print("玩游戏") 

play()
