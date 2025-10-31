# ============================== 1. 算术运算符 ==============================

a = 15
b = 4

# 加法 (+)
result_add = a + b    # 15 + 4 = 19
# 减法 (-)
result_sub = a - b    # 15 - 4 = 11
# 乘法 (*)
result_mul = a * b    # 15 * 4 = 60
# 除法 (/)：结果为浮点数
result_div = a / b    # 15 / 4 = 3.75
# 整除 (//)：向下取整
result_floordiv = a // b  # 15 // 4 = 3
# 取模 (%)：取余数
result_mod = a % b    # 15 % 4 = 3
# 幂运算 (**)：乘方
result_pow = a ** 2   # 15 ** 2 = 225

# 算术运算符的错误示例
# print(5 / 0)  # 错误：ZeroDivisionError: division by zero
# print(5 % 0)  # 错误：ZeroDivisionError: integer division or modulo by zero

# ============================== 2. 比较运算符 ==============================

x = 10
y = 20
z = 10

# 等于 (==)
bool_equal = (x == z)   # 10 等于 10，结果为 True
# 不等于 (!=)
bool_not_equal = (x != y)  # 10 不等于 20，结果为 True
# 大于 (>)
bool_greater = (y > x)    # 20 大于 10，结果为 True
# 小于 (<)
bool_less = (x < y)     # 10 小于 20，结果为 True
# 大于等于 (>=)
bool_greater_equal = (x >= z) # 10 大于等于 10，结果为 True
# 小于等于 (<=)
bool_less_equal = (y <= x)  # 20 小于等于 10，结果为 False

# 比较运算符的错误示例
# print(10 < 'hello') # 错误：TypeError: '<' not supported between instances of 'int' and 'str' (不同类型通常无法直接比较)

# ============================== 3. 逻辑运算符 ==============================

p = True
q = False

# 逻辑与 (and)：两边都为 True 才为 True
logic_and = p and q    # True and False，结果为 False
# 逻辑或 (or)：任意一边为 True 即为 True
logic_or = p or q     # True or False，结果为 True
# 逻辑非 (not)：取反
logic_not = not p     # not True，结果为 False

# 短路求值示例
# if 0 and (1 / 0): ... # 0 为 False，不会执行右边的除法，避免 ZeroDivisionError

# ============================== 4. 赋值运算符 ==============================

i = 5
j = 10

# 简单赋值 (=)
i = 7     # i 的值变为 7
# 加法赋值 (+=)
i += 3    # i = i + 3， i 的值变为 10
# 乘法赋值 (*=)
j *= 2    # j = j * 2， j 的值变为 20
# 除法赋值 (/=)
j /= 4    # j = j / 4， j 的值变为 5.0 (注意结果类型变为 float)
# 幂赋值 (**=)
j = 2
j **= 3   # j = j ** 3， j 的值变为 8

# 赋值运算符的错误示例
# 5 = 10  # 错误：SyntaxError: cannot assign to literal (不能给常量赋值)

# ============================== 5. 身份运算符 ==============================

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a  # c 和 a 引用同一个对象

# is：判断是否指向同一个内存地址
id_is = (list_a is list_b)  # 两个列表值相等，但不是同一个对象，结果为 False
id_is_same = (list_a is list_c) # 引用同一个对象，结果为 True

# is not：判断是否不指向同一个内存地址
id_is_not = (list_a is not list_b) # 结果为 True

# 注意：对于小整数或短字符串，Python 可能会进行优化，导致 is 结果为 True
int_1 = 100
int_2 = 100
int_is = (int_1 is int_2) # True (Python 优化)

# ============================== 6. 成员运算符 ==============================

my_list = ['apple', 'banana', 'cherry']
my_string = "Hello World"

# in：判断成员是否在序列中
member_in_list = ('banana' in my_list)   # 结果为 True
member_in_string = ('W' in my_string)    # 结果为 True
# not in：判断成员是否不在序列中
member_not_in_list = ('grape' not in my_list) # 结果为 True
member_not_in_string = ('z' not in my_string)  # 结果为 True
# 成员运算符的错误示例
# print('a' in 123)  # 错误：TypeError: argument of type 'int' is not iterable (整数类型不可迭代)
# print('a' not in None) # 错误：TypeError: argument of type 'NoneType' is not iterable (NoneType不可迭代)
