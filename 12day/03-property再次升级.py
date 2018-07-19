class Dog():

    def __init__(self):
        self.__age = 12

    @property
    def age(self):#把这个当做get方法
        return self.__age
  
    @age.setter
    def age(self,age):#把这个当做set方法
        if age > 0:
            self.__age = age

dog = Dog()
dog.age = 10#自己去调用set方法
print(dog.age)#自己去调用get方法

