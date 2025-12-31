"""
定义问候函数，根据传入的姓名和年龄，返回格式化的问候字符串
类型注解说明：
    name: str - 形参name要求传入字符串类型（姓名）
    age: int - 形参age要求传入整数类型（年龄）
        -> str - 函数返回值为字符串类型
"""
# Python 数据格式主要分为存储单一值的基础标量类型（int、float、str、bool、NoneType）
# 和存储多个值的容器聚合类型（list、tuple、dict、set、range 等）
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

"""
定义数据处理函数，支持处理整数列表或浮点/整数类型，最终返回浮点类型结果
类型注解说明：
    data: list[int] | float - 形参data支持两种类型（整数列表 或 浮点/整数类型，int可自动转为float）
        -> float - 函数返回值为浮点类型
"""
def process_data(data: list[int] | float) -> float:
    if isinstance(data, list):
        return sum(data) / len(data)
    return data * 1.0

#====================测试代码====================
print("=== 测试 greet() 问候函数 ===")
greet_result1 = greet("Guo Heng", 100)
print(f"测试用例输出：{greet_result1}")


greet_result1 = greet(1, 100)#会有爆黄，但是程序可以正常运行
print(f"测试用例输出：{greet_result1}")

print("=== 测试 process_data() 数据处理函数 ===")
data_list = [10, 20, 30, 40, 50]
process_result1 = process_data(data_list)
print(f"测试用例（传入列表 {data_list}）：平均值为 {process_result1}")
