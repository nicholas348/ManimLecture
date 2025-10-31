def decorator_example(func):#用于接受一个函数作为参数
    def wrapper(*args, **kwargs):#用于接受任意数量的位置参数和关键字参数
        print("Before calling the function")#装饰部分
        result = func(*args, **kwargs)
        print("After calling the function")#装饰部分
        return result
    return wrapper

@decorator_example
def say_hello(name):
    print(f"Hello, {name}!")#实际函数部分

say_hello("Alice")
print("----------------------------------------------------")


#带有参数的装饰器
def decorator_with_args(prefix):#可以是重复次数，也可以是日志前缀等
    def decorator(func):#用于接受一个函数作为参数
        def wrapper(*args, **kwargs):#用于接受任意数量的位置参数和关键字参数
            print(f"{prefix} Before calling the function")
            result = func(*args, **kwargs)
            print(f"{prefix} After calling the function")
            return result
        return wrapper
    return decorator

@decorator_with_args("LOG:")
def greet(name):#实际函数部分
    print(f"Greetings, {name}!")
greet("Bob")