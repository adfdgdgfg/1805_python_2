def fil(num):
    a,b = 0,1
    print("-------------1--------------")
    for i in range(num):
        print("----------2---------------")
        #print(b)
        yield b
        print("-----------3------------")
        a,b = b,a+b


#g = fil(8)
#print(g)
