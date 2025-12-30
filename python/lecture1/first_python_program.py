# 核心代码：print() 是 Python 中的「输出函数」，作用是把括号里的内容显示在屏幕上
# 括号里的 "helloworld" 是「字符串」，用英文双引号（""）或单引号（''）包裹，代表要输出的文本内容
# 考虑到大多数人的使用习惯，记得尽量使用双引号
print("hello world")
print('HELLO WORLD')
# 在刚刚的代码中，我们可以发现python是有自动换行机制的。而我们可以用编辑末行为的方式来免去自动换行
print("line_switch", end="")
print("LINE_SWITCH")
# 实现手动换行，我们需要在输出的语句中直接添加一个\n
print("enter\n\n\nENTER")
# 因为有两种不同的引号，我们可以通过嵌套引号的方式直接输出引号
print("'hello world'")
print('"hello world"')
# 当然，逃逸字符也可以用于输出在print语句中会被标记的特殊字符
print("\"")
print("\'")
print("\\n")