"""
将一个变量给芝指示为简单变量类型
"""

def greet(name: str, age: int) -> str:#将name变量指示为string,将age变量指示为int,输出指示为str
    return f"Hello {name}, you are {age} years old."

print(greet("k",10))
print(greet(1,1))#可以正常运行

"""
将一个变量给芝指示为复杂变量类型（变量组）
"""
def process_data(data: list[int] | float) -> float:#将data变量指示为由int组成的数组或float类型,输出指示为float
    if isinstance(data, list):#如果data是list类型的
        return sum(data) / len(data)
    return data * 1.0