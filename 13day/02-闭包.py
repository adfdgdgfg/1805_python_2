def test(num):
    def inner(x):
        print(x+num)
    return inner

t = test(1)
t(10)
