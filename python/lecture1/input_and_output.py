# 1. input() 函数：弹出输入提示框，等待用户在控制台输入一个数字
# 注意：用户输入的内容会以字符串类型返回，这是python唯一的输入格式
input("please enter a number: ")

# 2. print() 函数：在控制台直接输出字符串 "helloworld_1"，执行后自动换行
print("helloworld_1")

# 3. 定义一个字符串变量，变量名是 hello_world_text，变量值为 "helloworld_2"
# 变量命名遵循下划线命名法（小写字母+下划线），这是Python的推荐命名规范
# 在为字符串(在python中也可以直接称为变量)赋值时，程序都遵循将右边的赋给左边的的逻辑。
hello_world_text = "helloworld_2"

# 4. 打印上面定义的变量，输出变量存储的字符串值 "helloworld"
print(hello_world_text)

# 5. 定义第一个字符串变量 hello，存储值为 "Hello"
hello = "Hello"

# 6. 定义第二个字符串变量 world，存储值为 "World"
world = "World"

# 7. 连接字符串
print(hello + " " + world)# 方法一：在要连接的字符串之间写一个加号
print(f"{hello} {world}")# 方法二：使用f-string语法输出时，可以直接拼接由大括号包括的变量名
print(hello, world)# 方式三：在两个要连接的字符串的名字之间添加一个逗号隔开
