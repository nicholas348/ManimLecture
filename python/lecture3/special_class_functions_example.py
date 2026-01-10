class Vector:
    def __init__(self, x, y):
        """这个方法用于初始化vector"""
        self.x = x
        self.y = y

    def __repr__(self):
        """在print是输出什么"""
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        """在打印时输出什么"""
        return f"({self.x}i + {self.y}j)"

    def __add__(self, other):
        """在执行 + 运算时返回什么"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """在执行 - 运算是返回什么"""
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """判断是否相等的条件（==）"""
        return self.x == other.x and self.y == other.y
    def __len__(self):
        """输出长度"""
        # For a vector, let's return the number of dimensions
        return 2

    def __call__(self, scalar):
        """使得这个物体可以像函数一样被引用"""
        return Vector(self.x * scalar, self.y * scalar)


# --- Usage ---
v1 = Vector(2, 4)
v2 = Vector(1, 3)

print(f"v1: {v1}")               # Uses __str__ -> (2i + 4j)
print(f"Sum: {v1 + v2}")         # Uses __add__ -> (3i + 7j)
print(f"Equal? {v1 == v2}")      # Uses __eq__  -> False
print(f"Scaled: {v1(10)}")       # Uses __call__ -> (20i + 40j)

#保护方法
class MyClass:
    def __init__(self):
        self.public_data = "Everyone can see this"
        self._internal_data = "Please treat this as private"
        self.__more_internal_data = "Please treat this as most private. This is heavily protected"

    """
    无下划线：普通方法
    """
    def normal_method(self):
        return self.public_data

    """
    开发者不想让你引用的方法（可能随时都会改名或直接删掉）
    不建议引用
    """

    """
    单个下划线：保护方法
    """
    def _internal_method(self):
        return self._internal_data

    """
    二重下划线：加重保护
    """
    def __more_internal_method(self):
        return self.__more_internal_data

#调用普通方法
print(MyClass.normal_method(self=MyClass()))

#调用保护方法
print(MyClass._internal_method(self=MyClass()))

#调用加重保护方法
print(MyClass._MyClass__more_internal_method(self=MyClass()))