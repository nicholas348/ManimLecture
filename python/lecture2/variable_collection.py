#====================列表（List）- 有序、可变、支持混合类型元素====================


# 列表定义与类型转换
my_list = [1, 'two', 3.0, True] # 中括号内的四个元素就是列表里存储的4个元素。它们的类型分别是“int，string，float，bool”
print("1. 初始定义 my_list =", my_list)
# 元组转列表(元组的详细讲解在第二部分)
list_from_tuple = list((4, 5, 6))
print("2. 元组转列表 list_from_tuple =", list_from_tuple)
# 字符串转列表
list_from_str = list("abc")
print("3. 字符串转列表 list_from_str =", list_from_str)

print("-" * 20) # 输出了一条分界线

# 列表的核心操作方法(列表在读取元素的时候，会考虑其类型)
# 末尾追加元素
my_list.append('new')
print("4. append('new') 后 my_list =", my_list)
# 指定索引插入元素(被插入的元素将会在规定的索引位置出现，而原本的将会向后顺延一个)
my_list.insert(1, 'inserted')
print("5. insert(1, 'inserted') 后 my_list =", my_list)
# 连接列表(将extend中的列表接在原本的列表后面)
my_list.extend(["extended", 0.1])
print("6. extend([7, 8]) 后 my_list =", my_list)
# 移除并返回最后一个元素(也可以不保留被移除的元素)
pop_result = my_list.pop()
print("7. pop() 移除的元素 =", pop_result, "，pop() 后 my_list =", my_list)
# 移除第一个匹配项
my_list.remove('two')
print("8. remove('two') 后 my_list =", my_list)
# 替换某个索引对应的元素
my_list[0] = 100
print("9. 修改索引0为100 后 my_list =", my_list)
# 查找元素首次出现的索引
list_index = my_list.index(3.0)
print("10. 3.0 在 my_list 中的索引 list_index =", list_index)
# 统计元素出现次数
list_count = my_list.count(1)
print("11. 1 在 my_list 中出现的次数 list_count =", list_count)
# 获取列表长度
list_len = len(my_list)
print("12. my_list 的长度 list_len =", list_len)

# 列表排序与推导式
list_disorderd = [1, 15, 2, 4, 9, 6]
print("13. 初始无序列表 list_disorderd =", list_disorderd)
# 按照升序排列
list_disorderd.sort()
print("14. sort() 升序排序后 list_disorderd =", list_disorderd)
# 借助循环生成函数
# 组成部分[<表达式> for <循环变量> in <循环可迭代对象>]
list_for_loop = [i**2 for i in range(5)] # 被循环的值来自range(5)。是“0，1，2，3，4”
print("15. 0~4平方列表推导式 list_for_loop =", list_for_loop)
# 嵌套列表推导式
another_list_for_loop = [[j for j in range(i)] for i in range(10)]# 这个输出的第一元素是空元素，这是因为第一次传到内从循环(j的循环)的值为0。执行循环0次，自然这一项里面没有元素
print("16. 嵌套列表推导式 another_list_for_loop =", another_list_for_loop)
# 生成重复元素列表
list_for_loop_3 = [3 for i in range(10)]
print("17. 10个3重复列表 list_for_loop_3 =", list_for_loop_3)


#====================元组（Tuple）- 有序、不可变、支持混合类型元素====================


# 元组定义与类型转换
my_tuple = (1, 'two', 3.0)
single_element_tuple = (42,)  # 单元素元组必须带逗号
tuple_from_list = tuple([5, 6, 7])  # 列表转元组

# 元组的核心操作方法
tuple_concat = my_tuple + (4,)  # 元组拼接（生成新元组，原元组不变）
tuple_count = my_tuple.count('two')  # 统计元素出现次数
tuple_index = my_tuple.index(3.0)  # 查找元素首次出现的索引
tuple_len = len(my_tuple)  # 获取元组长度
tuple_index_access = my_tuple[0]  # 索引访问元素（仅可读）


#====================集合（Set）- 无序、可变、无重复、元素必须不可变====================
# 集合定义与类型转换
my_set = {1, 2, 'three', 4}
set_from_list = set([4, 5, 5, 6])  # 列表转集合（自动去重）
empty_set = set()  # 创建空集合（{}创建空字典）

# 集合的基础操作方法
my_set.add(5)  # 添加单个元素
my_set.remove(4)  # 移除元素（元素不存在报错）
my_set.discard(1)  # 移除元素（元素不存在不报错）
if my_set:  # 避免空集合pop报错
    set_pop = my_set.pop()  # 随机移除并返回一个元素
set_len = len(my_set)  # 获取集合长度
my_set.clear()  # 清空集合

# 集合的关系运算
set_A = {1, 2, 3}
set_B = {3, 4, 5}
set_union = set_A.union(set_B)  # 并集
set_intersection = set_A.intersection(set_B)  # 交集
set_difference = set_A.difference(set_B)  # 差集（A有B无）
set_issubset = set_A.issubset({1, 2, 3, 4})  # 判断是否为子集


#====================字典（Dictionary）- 键值对映射、可变、键必须不可变====================


# 字典定义与类型转换
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
dict_from_pairs = dict([('a', 1), ('b', 2)])  # 元组列表转字典
dict_from_kwargs = dict(fruit='apple', color='red')  # 关键字参数创建字典
empty_dict = {}  # 创建空字典

# 字典的访问与查询
dict_value = my_dict['name']  # 键访问值（键不存在报错）
dict_safe_get = my_dict.get('country', 'USA')  # 安全访问（默认值兜底）
dict_keys = my_dict.keys()  # 获取所有键
dict_values = my_dict.values()  # 获取所有值
dict_items = my_dict.items()  # 获取所有键值对
dict_len = len(my_dict)  # 获取字典长度（键值对个数）

# 字典的修改、添加与移除
my_dict['age'] = 26  # 修改现有键的值
my_dict['email'] = 'alice@example.com'  # 添加新键值对
dict_pop_value = my_dict.pop('city')  # 移除并返回指定键的值
my_dict.update({'age': 27, 'zip': 10001})  # 合并/更新字典（存在则改，不存在则加）
my_dict.clear()  # 清空字典
