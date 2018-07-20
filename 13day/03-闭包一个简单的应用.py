def test(a,b):
    def inner(x):
        return a*x+b

    return inner



t = test(1,1)
print(t(2))
print(t(3))

def test1(a,b,x):
    return a*x+b

print(test1(1,1,2))
print(test1(1,1,3))
