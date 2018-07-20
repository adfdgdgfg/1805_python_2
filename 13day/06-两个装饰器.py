#定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

#定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold#test1 = makeBold(test1)
def test1():
    return "hello world-1"

@makeItalic#test2 = makeItalic(test2)
def test2():
    return "hello world-2"

@makeBold
@makeItalic
def test3():
    return "hello world-3"

#    <i><b>"hello world-3"</b></i>
#    <b><i>"hello world-3"</i></b>

print(test1())
print(test2())
print(test3())
