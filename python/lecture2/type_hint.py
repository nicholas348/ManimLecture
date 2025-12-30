def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

def process_data(data: list[int] | float) -> float:
    if isinstance(data, list):
        return sum(data) / len(data)
    return data * 1.0