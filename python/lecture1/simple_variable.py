"""
--- 1. 整数 (int) ---
"""

"""
整数定义与类型转换
"""
my_first_int = 42
my_second_int = 3
my_third_int = 3 * (10**10) + 1  # 大整数
my_fouth_int, my_fifth_int = -7, 0  # 负整数和零

"""
整数的算术方法
"""
number_one = 25
number_two = 4
number_add = number_one + number_two  # 加法 (结果: 29)
number_sub = number_one - number_two  # 减法 (结果: 21)
number_mul = number_one * number_two  # 乘法 (结果: 100)
number_div = number_one / number_two  # 除法，结果为浮点数 (结果: 6.25)
number_floordiv = number_one // number_two  # 整除，结果为整数 (结果: 6)
number_mod = number_one % number_two  # 取模/余数 (结果: 1)
number_pow = number_one ** number_two  # 乘方 (结果: 625)
number_abs = abs(-5) # 绝对值 (结果: 5)
int_bit_length = (10).bit_length() # 返回表示该整数所需的最小位数 (结果: 4, 10的二进制是1010)

"""
整数的常见错误
print(int("abc"))       # 错误：ValueError: invalid literal for int()
print(int("12.34"))     # 错误：ValueError: invalid literal for int()
print(int(""))          # 错误：ValueError: invalid literal for int()
print(42 / 0)           # 错误：ZeroDivisionError: division by zero
"""

"""
--- 2. 浮点数 (float) ---
"""

"""
浮点数定义与类型转换
"""
first_float = 1.5
second_float = 0.5
float_scientific = 3e10  # 科学计数法 (结果: 30000000000.0)
float_from_scientific_str = float("3e10") # string转float (结果: 30000000000.0)

"""
浮点数的算术方法
"""
float_add = first_float + second_float  # 加法 (结果: 2.0)
float_sub = first_float - second_float  # 减法 (结果: 1.0)
float_mul = first_float * second_float  # 乘法 (结果: 0.75)
float_div = first_float / second_float  # 除法 (结果: 3.0)
float_floordiv = first_float // second_float  # 整除，结果仍为浮点数 (结果: 3.0)
float_mod = first_float % second_float  # 取模 (结果: 0.0)
float_pow = first_float ** second_float  # 乘方 (结果: 1.224744871391...)
float_is_integer = (3.0).is_integer() # 判断浮点数是否可以精确表示为整数 (结果: True)
float_from_int = float(3)  # int转float (结果: 3.0)
int_from_float = int(2.47)  # float转int, 截断小数部分 (结果: 2)
int_from_neg_float = int(-2.54)  # 负float转int, 截断小数部分 (结果: -2)

"""
浮点数的常见错误

print(5.0 / 0)          # 结果为 float('inf')，不是错误，但需注意
"""

"""
 --- 3. 字符串 (string) ---
"""
"""
字符串定义与类型转换
"""
first_string = "Hello"
second_string = 'World'
str_from_int = str(123)  # int转str (结果: '123')
str_from_float = str(45.67)  # float转str (结果: '45.67')
int_from_string = int("89")  # string转int (结果: 89)
float_from_string = float("3.14")  # string转float (结果: 3.14)

"""
字符串的方法
"""
string_concat = first_string + " " + second_string  # 拼接 (结果: 'Hello World')
string_repeat = first_string * 3  # 重复 (结果: 'HelloHelloHello')
string_len = len(first_string)  # 长度 (结果: 5)
string_upper = first_string.upper()  # 转换为大写 (结果: 'HELLO')
string_lower = string_upper.lower()  # 转换为小写 (结果: 'hello')
string_strip = "  padded  ".strip()  # 移除两侧空白 (结果: 'padded')
string_split = "a,b,c".split(',')  # 分割成列表 (结果: ['a', 'b', 'c'])
string_join = "-".join(['a', 'b', 'c'])  # 列表元素用字符串连接 (结果: 'a-b-c')
string_replace = "Python".replace("P", "J") # 替换 (结果: 'Jython')
string_find = "apple".find("pl") # 查找子串，返回起始索引 (结果: 2)
string_startswith = "file.txt".startswith("file") # 检查开头 (结果: True)
string_format = "Name: {}, Age: {}".format("Bob", 30) # 格式化 (结果: 'Name: Bob, Age: 30')
string_index = first_string[1] # 索引取值 (结果: 'e')
string_slice = first_string[1:4] # 切片取值 (结果: 'ell')
"""
字符串的常见错误
print(float("xyz"))     # 错误：ValueError: could not convert string to float: 'xyz'
print(float("56.78abc")) # 错误：ValueError: could not convert string to float: '56.78abc'
print(float(""))        # 错误：ValueError: could not convert string to float: ''
first_string[0] = 'h'    # 错误：TypeError: 'str' object does not support item assignment (字符串是不可变类型)
print("abc" - "a")       # 错误：TypeError: unsupported operand type(s) for -: 'str' and 'str'
print(first_string[10])  # 错误：IndexError: string index out of range
"""

"""
--- 4. 布尔值 (bool) ---
"""

"""
布尔值定义与类型转换
"""
first_bool = True
second_bool = False
bool_from_one = bool(1)  # 非0数字转True (结果: True)
bool_from_zero = bool(0)  # 0转False (结果: False)
bool_from_neg = bool(-1)  # 负数转True (结果: True)
bool_from_empty_str = bool("")  # 空字符串转False (结果: False)
bool_from_non_empty_str = bool("False")  # 非空字符串转True (结果: True)

int_from_bool = int(False)  # bool转int, False=0, True=1 (结果: 0)
"""
布尔值的逻辑方法
"""

bool_and = first_bool and second_bool  # 逻辑与 (结果: False)
bool_or = first_bool or second_bool  # 逻辑或 (结果: True)
bool_not = not first_bool  # 逻辑非 (结果: False)
bool_equal = (1 == 1) # 比较 (结果: True)

"""
布尔值的常见错误 (bool常作为条件使用，直接的操作错误较少)
bool_add = True + False  不常见，但可执行，True=1, False=0 (结果: 1)
print(bool("abc") * 2)  可执行，True=1 (结果: 2)
"""


"""
--- 5. 复数 (complex) ---
"""
"""
复数定义
"""
first_complex = 3 + 4j
second_complex = complex(1, 2)  # complex(real, imag) (结果: 1+2j)

"""
复数的方法
"""
complex_add = first_complex + second_complex  # 加法 (结果: 4+6j)
complex_mul = first_complex * second_complex  # 乘法 (结果: -5+10j)
complex_real = first_complex.real  # 实部 (结果: 3.0)
complex_imag = first_complex.imag  # 虚部 (结果: 4.0)
complex_conj = first_complex.conjugate()  # 共轭复数 (结果: 3-4j)

"""
复数的常见错误
print(3 + j)             # 错误：NameError: name 'j' is not defined (虚部必须有数字)

print(complex("abc"))  # 错误：ValueError: complex() arg is a malformed string
print(complex("1+2i")) # 错误：ValueError: complex() arg is a malformed string (必须用j表示虚部)
"""

number_none = None
bool_none = bool(number_none)  # None转bool (结果: False)
"""
print(number_none + 1)       错误
print(int(number_none)  错误
print(float(number_none)) 错误
print(str(number_none)) 'None'
"""
