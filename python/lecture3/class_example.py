
class Dog:#定义了一个名为Dog的类
    dog_amount=0
    def __new__(cls, breed, age):
        # 改变这个类的特征（例如个数）
        print("Creating a new Dog instance")
        cls.dog_amount += 1
        # 必须调用父类的__new__方法来创建实例
        instance = super().__new__(cls)
        return instance

    # 定义了一个类Dog的初始化方法，接受两个参数breed和age
    def __init__(self,breed, age):
        self.age = age
        self.breed = breed

    # 定义了一个方法get_age，用于返回狗的年龄
    def get_age(self):
        return self.age

    # 定义了一个方法get_breed，用于返回狗的品种
    def get_breed(self):
        return self.breed

    # 定义了一个方法eat，表示狗在吃东西
    def eat(self):
        print(f"{self.breed} is eating")

    # 定义了一个方法sleep，表示狗在睡觉
    def sleep(self):
        print(f"{self.breed} is sleeping")

#创建了一个Dog类的实例my_dog1，品种为"bulldog"，年龄为4
my_dog1 = Dog("bulldog", 4)

#创建了一个Dog类的实例my_dog2，品种为"chihuahua"，年龄为2
my_dog2 = Dog("chihuahua", 2)

#创建了一个Dog类的实例my_dog3，品种为"husky"，年龄为6
my_dog3 = Dog("husky", 6)

#让my_dog2对象调用eat方法，输出"chihuahua is eating"
my_dog2.eat()







class AlaskaMalamute(Dog):#定义了一个名为AlaskaMalamute的类，继承自Dog类
    breed = "Alaska Malamute"#在AlaskaMalamute类中定义了一个属性breed，值为"Alaska Malamute"

    def __new__(cls, age):
        return super().__new__(cls,"Alaska Malamute",age)
    def __init__(self, age):  # 定义了AlaskaMalamute类的初始化方法，接受一个参数age
        # 调用父类Dog的初始化方法，传入类名.breed和age参数
        super().__init__(self.breed, age)

    # 定义了一个方法work，表示狗在工作
    def work(self):
        print(f"{self.breed} is working in snow")

    # 重写了父类Dog的eat方法，表示Alaska Malamute吃得很多
    def eat(self):
        print(f"{self.breed} is eating a lot")

# 创建了一个AlaskaMalamute类的实例my_dog4，年龄为5
my_dog4 = AlaskaMalamute(age=5)

#让my_dog4对象调用eat方法，输出"Alaska Malamute is eating a lot"
my_dog4.eat()
#让my_dog4对象调用work方法，输出 "Alaska Malamute is working in snow"
my_dog4.work()
#让my_dog4对象调用sleep方法，输出"Alaska Malamute is sleeping"
my_dog4.sleep()

#访问my_dog4对象的breed属性，返回"Alaska Malamute"
print(my_dog4.breed)

