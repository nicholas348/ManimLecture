def prod_of_num(*args):#元组输入
    res = 1
    for i in args:
        res *= i
    return res
print(prod_of_num(1,2,3,4,5))


print("----------------------------------------------")
def args_example(**kwargs):#字典输入
    for key, value in kwargs.items():
        print(f"the {key} is {value}")
args_example(name="Alice", age=30, city="New York")

print("----------------------------------------------")
def kw_only_example(arg1, *, kw_only_arg1, kw_only_arg2="default"):#仅关键字输入
    print(f"arg1: {arg1}")
    print(f"kw_only_arg1: {kw_only_arg1}")
    print(f"kw_only_arg2: {kw_only_arg2}")
kw_only_example(10, kw_only_arg1="Hello")

print("----------------------------------------------")
def mixed_arguments(arg1, *args, kw_only_arg, **kwargs):#混合输入
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"kw_only_arg: {kw_only_arg}")
    print(f"kwargs: {kwargs}")
mixed_arguments(1, 2, 3, kw_only_arg=" ", name="Bob", age=25)

print("----------------------------------------------")
def type_hint_example(name: str, age: int) -> str:#类型提示
    return f"{name} is {age} years old."
print(type_hint_example("Charlie", 28))
print(type_hint_example(123, "Twenty")) # 运行时不会报错，但不符合类型提示 最好不要这样做

