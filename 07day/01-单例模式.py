class Cat():
    __instance  = None
    __flag  = False
    def __new__(cls,*args,**kwargs):
        if cls.__instance == None:
            cls.__instance =  object.__new__(cls)
            return cls.__instance#第一次
        else:
            return cls.__instance#除了第一次

    def __init__(self,name):
        if Cat.__flag == False:
            self.name = name
            Cat.__flag = True



tom = Cat("tom")
print(id(tom))
tom1 = Cat("tom1")
print(id(tom1))

print(tom.name)
print(tom1.name)
