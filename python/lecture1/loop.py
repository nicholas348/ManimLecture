# 定义分割线变量。因为程序中需要大量分割线，这样可以提高代码美观度和可读性。
separator = "-----------------------------------------------------------------------------"



"""
====================PART I: 按照次数循环====================
"""




"""
示例1：基础的循环定义循环的次数。
注意：计数器从0开始！！！
"""
for loop_time in range(5):
    print("Loop time:", loop_time)  # 打印当前循环的次数（0到4）
print(separator)  # 打印分割线

"""
# 示例2：带步长的for循环，range(0, 10, 2)表示从0开始，到10结束（不包含10），步长为2
# 生成的序列是0、2、4、6、8，循环执行5次
"""

for loop_time in range(0, 10, 2):
    print("Loop time:", loop_time)  # 打印当前循环的数值（0到8）
print(separator)  # 打印分割线

"""
示例3：用下划线作为循环变量，表明该变量仅用于控制循环次数，无需在循环内使用其值
range(10)生成0-9的序列，循环执行10次
这样写可以省下一个变量的内存。python中的变量相比于别的语言内存占用偏大。在一些大型程序中应使用这种方法来节省内存。
"""
for _ in range(10):
    print(0)  # 每次循环都打印数字0，共打印10次
print(separator)  # 打印分割线

"""
示例4：基础while循环，通过变量条件控制循环次数
注意：while循环一般被用于需要进行bool运算的循环中(即需要判断更复杂结束条件的)。很少用于完成基于次数的循环。
"""
value = 0  # 初始化循环控制变量value为0
while value < 5:  # 循环条件：当value小于5时，继续执行循环体
    print(f"While loop value:{value}")  # 打印当前while循环的变量值
    value += 1  # 循环变量自增1（避免无限循环），等价于value = value + 1
print(separator)  # 打印分割线




"""
====================PART II: 循环的手动跳出====================
"""



# 示例5：在for循环中用break语句，跳出循环
for loop in range(10):  # loop依次取0-9的整数，计划循环10次
    print(f"iteration time:{value}")  # 打印当前迭代次数值
    if loop >= 7:  # 判断条件：当循环变量loop大于或等于7时
        break  # 执行break语句，跳出for循环，直接开始执行循环后面的内容。
    print("program actually executed")  # 仅当loop<7时，才会
print(separator)  # 打印分割线
# 特别说明：因为value变量没有被重置，且在示例4中，它的值已经变成了5。所以第一次输出的是5。

"""
示例6：for循环中使用continue语句，结束当前这一次循环
"""
for loop in range(10):  # loop依次取0-9的整数，循环执行10次
    print(f"iteration time:{loop}")  # 打印当前循环的迭代次数（0-9）
    if loop >= 7:  # 判断条件：当循环变量loop大于或等于7时
        continue  # 执行continue语句，跳过当前循环后续代码，直接进入下一次循环
    print("program actually executed")  # 仅当loop<7时（0-6），才会执行该行打印，7-9次循环会跳过该行
print(separator)  # 打印分割线

"""
示例7：while循环中使用break语句，强制终止整个while循环
"""
value = 0  # 初始化循环控制变量value为0
while value < 10:  # 循环条件：value小于10时，执行循环体
    print(f"while loop value:{value}")  # 打印当前while循环的变量值
    if value == 5:  # 判断条件：当value等于5时
        break  # 执行break语句，立即终止整个while循环
    print(f"program actually executed")  # 仅当value≠5且value<10时（0-4），才会执行该行打印
    value += 1  # 循环变量+1
print(separator)  # 打印分割线

"""
# 示例8：while循环中使用continue语句，跳过当前循环剩余代码，进入下一次循环
"""
value = 0  # 初始化循环控制变量value为0
while value < 10:  # 循环条件：value小于10时，执行循环体
    print(f"while loop value:{value}")  # 打印当前while循环的变量值（0-9）
    if value == 5:  # 判断条件：当value等于5时
        value += 1  # 先将value自增1（避免卡在5导致无限循环）
        continue  # 执行continue语句，跳过当前循环后续代码，直接进入下一次循环判断
    print(f"program actually executed")  # 仅当value≠5且value<10时，才会执行该行打印
    value += 1  # 循环变量自增1
print(separator)  # 打印分割线




"""
====================PART III: 死循环(无限循环)====================
"""




"""
# 在一些特定情况下，我们希望程序进行无限循环
# 使用无限循环（while True）持续接收输入
"""
while True:
    # 接收用户输入的字符串，input()函数会等待用户输入并返回输入内容
    user_input = input("请输入一个字符串（输入'stop'终止程序）：")
    # 判断用户输入是否为"stop"（不区分大小写可选，此处默认严格匹配小写stop）
    if user_input == "stop":  #这里是终止条件
        print("程序接收到'stop'，即将终止...")
        break  # 跳出无限循环，程序结束
    # 若输入不是stop，打印用户输入的内容，继续下一次循环
    print(f"你输入的字符串是：{user_input}")

# 说明：当然，直接终止程序也是可以将其关闭的
# 在写程序时，应尽量避免使用死循环。死循环会导致大量的资源占用。可能会导致出现电脑卡死或程序未响应等问题。
# 警告：在使用死循环时，一定要写跳出条件！！！
