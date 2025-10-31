for loop_time in range(5):#从0~4循环
    print("Loop time:", loop_time)


print("------------------------------------------------------------------------------")
for loop_time in range(0, 10, 2):#从0~9循环，步长为2
    print("Loop time:", loop_time)


for loop_time in range(5):#从0~4循环
    print("Loop time:", loop_time)


print("------------------------------------------------------------------------------")

list_for_loop = [i**2 for i in range(5)]#列表推导式，生成0~4的平方列表
#list_for_loop = [0, 1, 4, 9, 16]

another_list_for_loop = [[j for j in range(i)] for i in range(10)]
#another_list_for_loop  = [[0],[0,1],[0,1,2],....,[0,1,2,3,4,5,6,7,8,9]]
list_for_loop_3 = [3 for i in range(10)]
#list_for_loop = [3,3,3,3,3,3,3,3,3,3]

print("------------------------------------------------------------------------------")
value = 0
while value < 5:#当value小于5时循环
    print(f"While loop value:{value}")
    value += 1#i自增1
#注意避免死循环

print("------------------------------------------------------------------------------")
#break:直接跳出循环
for loop in range(10):
    print(f"iteration time:{value}")
    if loop>=7:
        break
    print("program actually executed")#如果输出，则为执行。如果没有输出，则没有执行

print("------------------------------------------------------------------------------")
#continue：进入下一个循环
for loop in range(10):
    print(f"iteration time:{loop}")
    if loop>=7:
        continue
    print("program actually executed")#如果输出，则为执行。如果没有输出，则没有执行

print("------------------------------------------------------------------------------")
# break 在 while中的情况
value = 0
while value <10:
    print(f"while loop value:{value}")
    if value==5:
        break
    print(f"program actually executed")
    value+= 1

print("------------------------------------------------------------------------------")
#continue 在 while中的情况
value = 0
while value <10:
    print(f"while loop value:{value}")
    if value==5:
        continue
    print(f"program actually executed")
    value+= 1



