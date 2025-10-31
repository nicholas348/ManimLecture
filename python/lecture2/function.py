def absolute_value(x):#定义了一个计算绝对值的函数
    if x < 0:
        return -x
    else:
        return x

absolute_value(-3) #返回3
absolute_value(5)  #返回5

def muti_variable_function(a, b):#定义了一个多个变量的函数
    return a^2+b^2


def factorial(n):#定义了一个计算阶乘的递归函数
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)
#5>0 #返回5*factorial(4)
#4>0 #返回5*4*factorial(3)
#3>0 #返回5*4*3*factorial(2)
#2>0 #返回5*4*3*2*factorial(1)
#1>0 #返回5*4*3*2*1*factorial(0)
#0==0 #返回5*4*3*2*1*1
#最终结果为5*4*3*2*1*1=120




def Fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

Fibonacci(6)#=8
