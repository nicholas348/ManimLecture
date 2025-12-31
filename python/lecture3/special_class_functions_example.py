class Vector:
    def __init__(self, x, y):
        """这个方法用于初始化vector"""
        self.x = x
        self.y = y

    def __repr__(self):
        """Official string representation for developers (used in console)."""
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        """在打印时输出什么"""
        return f"({self.x}i + {self.y}j)"

    def __add__(self, other):
        """在+时返回什么"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """在-是返回什么"""
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """判断是否相等（==）"""
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