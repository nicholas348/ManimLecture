for loop_time in range(5):#从0~4循环
    print("Loop time:", loop_time)


print("------------------------------------------------------------------------------")
for loop_time in range(0, 10, 2):#从0~9循环，步长为2
    print("Loop time:", loop_time)

for loop_time in range(5):#从0~4循环
    print("Loop time:", loop_time)




print("------------------------------------------------------------------------------")
#打印1 10次
for _ in range(10):
    print(1)



print("------------------------------------------------------------------------------")



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
        value += 1
        continue
    print(f"program actually executed")
    value+= 1



