class Dog():

    def __init__(self):
        self.__age = 12#私有属性
        self.name = "tom"#公有属性
    
    def getAge(self):
        return self.__age

    def setAge(self,age):
        if age > 0:
            self.__age = age


dog = Dog()
#print(dog.__age)
#dog.setAge(10)
#dog.__age = 10#添加新的属性，新属性也叫__age
print(dog.getAge())
print(dog.name)
