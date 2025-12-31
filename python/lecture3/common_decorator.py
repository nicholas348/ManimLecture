

class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    # 1. @property - Turns a method into a read-only attribute
    @property
    def radius(self) -> float:
        return self._radius

    # 2. @property.setter - Allows you to add logic when setting a value
    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    # 3. @staticmethod - A method that doesn't need access to 'self' or 'cls'
    @staticmethod
    def is_valid_radius(value: float) -> bool:
        return value > 0

    # 4. @classmethod - Receives the class (cls) as the first argument
    @classmethod
    def from_diameter(cls, diameter: float):
        return cls(diameter / 2)

# 5. @functools.lru_cache - Caches function results to save time on heavy tasks

"""
使用特例--- Usage Examples ---
"""

"""
设置特征
"""
c = Circle(5)
print(f"Initial Radius: {c.radius}")
c.radius = 10  # Uses the setter
print(f"Updated Radius: {c.radius}")

"""
class的方法
"""
print(f"Is -5 valid? {Circle.is_valid_radius(-5)}")

# Class Method
c2 = Circle.from_diameter(20)
print(f"Radius from diameter 20: {c2.radius}")

