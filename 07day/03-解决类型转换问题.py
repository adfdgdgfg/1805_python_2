class Tool():

    def num(self):
        n = input("请输入一个数字")
        if n.isdigit():
            print(int(n)+1)
        else:
            print("不合法")

    def num1(self):
        try:
            n = int(input("请输入一个数字"))
            print(n+1)
        except ValueError:
            print("不合法")

tool = Tool()
tool.num1()



