class Dog():

    def __init__(self):
        self.__age = 12


    def getAge(self):
        return self.__age

    def setAge(self,age):
        if age > 0:
            self.__age = age

    age = property(getAge,setAge)#把get和set方法升级，可以直接通过一个属性实现调用和赋值
dog = Dog()
#dog.setAge(100)
#print(dog.getAge())

dog.age = 10#自己去调用set方法
print(dog.age)#自己去调用get方法

