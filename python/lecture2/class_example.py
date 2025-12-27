class Dog:#定义了一个名为Dog的类
    def __init__(self,breed, age):#定义了一个类Dog的初始化方法，接受两个参数breed和age
        self.age = age
        self.breed = breed

    def get_age(self):#定义了一个方法get_age，用于返回狗的年龄
        return self.age
    def get_breed(self):#定义了一个方法get_breed，用于返回狗的品种
        return self.breed
    def eat(self):#定义了一个方法eat，表示狗在吃东西
        print(f"{self.breed} is eating")
    def sleep(self):#定义了一个方法sleep，表示狗在睡觉
        print(f"{self.breed} is sleeping")

my_dog1 = Dog("bulldog", 4)#创建了一个Dog类的实例my_dog1，品种为"bulldog"，年龄为4
my_dog2 = Dog("chihuahua", 2)#创建了一个Dog类的实例my_dog2，品种为"chihuahua"，年龄为2
my_dog3 = Dog("husky", 6)#创建了一个Dog类的实例my_dog3，品种为"husky"，年龄为6

my_dog2.eat()#让my_dog2对象调用eat方法，输出"chihuahua is eating"







class AlaskaMalamute(Dog):#定义了一个名为AlaskaMalamute的类，继承自Dog类
    breed = "Alaska Malamute"#在AlaskaMalamute类中定义了一个属性breed，值为"Alaska Malamute"
    def __init__(self, age):#定义了AlaskaMalamute类的初始化方法，接受一个参数age
        super().__init__(self.breed, age)#调用父类Dog的初始化方法，传入breed和age参数

    def work(self):#定义了一个方法work，表示狗在工作
        print(f"{self.breed} is working in snow")
    def eat(self):
        print(f"{self.breed} is eating a lot")#重写了父类Dog的eat方法，表示Alaska Malamute吃得很多
    def __add__(self):
        self.age +=1
my_dog4 = AlaskaMalamute(5)#创建了一个AlaskaMalamute类的实例my_dog4，年龄为5
my_dog4.eat()#让my_dog4对象调用eat方法，输出"Alaska Malamute is eating a lot"
my_dog4.work()#让my_dog4对象调用work方法，输出 "Alaska Malamute is working in snow"
my_dog4.sleep()#让my_dog4对象调用sleep方法，输出"Alaska Malamute is sleeping"
print(my_dog4.breed)#访问my_dog4对象的breed属性，返回"Alaska Malamute"

