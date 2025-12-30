# 列表定义与类型转换
my_list = [1, 'two', 3.0, True]
list_from_tuple = list((4, 5, 6))  # tuple转list (结果: [4, 5, 6])
list_from_str = list("abc") # string转list (结果: ['a', 'b', 'c'])

# 列表的方法 (列表是可变类型)
my_list.append('new')  # 添加到末尾 (my_list: [1, 'two', 3.0, True, 'new'])
my_list.insert(1, 'inserted')  # 插入到指定位置 (my_list: [1, 'inserted', 'two', 3.0, True, 'new'])
my_list.extend([7, 8])  # 扩展列表 (my_list: [..., 'new', 7, 8])
my_list.pop()  # 移除并返回最后一个元素 (返回: 8, my_list: [..., 'new', 7])
my_list.remove('two')  # 移除第一个匹配项 (my_list: [1, 'inserted', 3.0, True, 'new', 7])
my_list[0] = 100  # 修改元素 (my_list: [100, 'inserted', 3.0, True, 'new', 7])
list_index = my_list.index(3.0)  # 查找元素索引 (结果: 2)
list_count = my_list.count(7)  # 元素出现次数 (结果: 1)
list_len = len(my_list) # 长度 (结果: 6)
list_disorderd = [1,15,2,4,9,6]
list_disorderd.sort()#list = disorderd = [1,2,4,6,9,15]
list_for_loop = [i**2 for i in range(5)]#列表推导式，生成0~4的平方列表
#list_for_loop = [0, 1, 4, 9, 16]

another_list_for_loop = [[j for j in range(i)] for i in range(10)]
#another_list_for_loop  = [[0],[0,1],[0,1,2],....,[0,1,2,3,4,5,6,7,8,9]]
list_for_loop_3 = [3 for i in range(10)]
#list_for_loop = [3,3,3,3,3,3,3,3,3,3]

# 列表的常见错误
# print(my_list.remove('missing')) # 错误：ValueError: list.remove(x): x not in list
# print(my_list[10])             # 错误：IndexError: list index out of range
# list_from_tuple.sort(key=str)  # 错误：TypeError: '<' not supported between instances of 'str' and 'int' (如果元素类型不同)

# --- 7. 元组 (tuple) ---

# 元组定义与类型转换
my_tuple = (1, 'two', 3.0)
single_element_tuple = (42,)  # 包含单个元素的元组必须带逗号
tuple_from_list = tuple([5, 6, 7])  # list转tuple (结果: (5, 6, 7))

# 元组的方法 (元组是不可变类型)
tuple_concat = my_tuple + (4,)  # 拼接 (结果: (1, 'two', 3.0, 4))
tuple_count = my_tuple.count('two')  # 元素出现次数 (结果: 1)
tuple_index = my_tuple.index(3.0)  # 查找元素索引 (结果: 2)
tuple_len = len(my_tuple) # 长度 (结果: 3)
tuple_index_access = my_tuple[0] # 索引取值 (结果: 1)

# 元组的常见错误
# my_tuple[0] = 100        # 错误：TypeError: 'tuple' object does not support item assignment (元组是不可变类型)
# my_tuple.append(4)       # 错误：AttributeError: 'tuple' object has no attribute 'append'
# my_tuple.remove(1)       # 错误：AttributeError: 'tuple' object has no attribute 'remove'

# --- 8. 集合 (set) ---

# 集合定义与类型转换
my_set = {1, 2, 'three', 4}
#set_from_list = set([4, 5, 5, 6])  # list转set，自动去重 (结果: {4, 5, 6})
empty_set = set() # 创建空集合必须使用set()，{}创建的是空字典

# 集合的方法 (集合是可变类型，元素必须是不可变类型)
my_set.add(5)  # 添加元素 (my_set: {1, 2, 4, 5, 'three'})
my_set.remove(4)  # 移除元素，若元素不存在会报错 (my_set: {1, 2, 5, 'three'})
my_set.discard(1)  # 移除元素，若元素不存在不会报错 (my_set: {2, 5, 'three'})
set_pop = my_set.pop()  # 随机移除并返回一个元素 (返回: 2或5或'three')
set_len = len(my_set) # 长度 (结果: 2或3)
set_clear = my_set.clear() # 清空集合 (my_set: set())

set_A = {1, 2, 3}
set_B = {3, 4, 5}
set_union = set_A.union(set_B)  # 并集 (结果: {1, 2, 3, 4, 5})
set_intersection = set_A.intersection(set_B)  # 交集 (结果: {3})
set_difference = set_A.difference(set_B)  # 差集 (结果: {1, 2})
set_issubset = set_A.issubset({1, 2, 3, 4}) # 是否为子集 (结果: True)

# 集合的常见错误
# my_set.add([1, 2])       # 错误：TypeError: unhashable type: 'list' (集合元素必须是不可变类型)
# print(set_A[0])          # 错误：TypeError: 'set' object is not subscriptable (集合不支持索引操作)
# print(set_A.remove(10))  # 错误：KeyError: 10 (remove找不到元素会报错)



# --- 9. 字典 (dictionary) ---

# 字典定义与类型转换 (字典是可变类型，以键值对存储)
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
dict_from_pairs = dict([('a', 1), ('b', 2)])  # 从元组列表创建 (结果: {'a': 1, 'b': 2})
dict_from_kwargs = dict(fruit='apple', color='red') # 使用关键字参数创建 (结果: {'fruit': 'apple', 'color': 'red'})
empty_dict = {} # 创建空字典

# 字典的访问与方法
dict_value = my_dict['name']  # 通过键访问值 (结果: 'Alice')
dict_safe_get = my_dict.get('country', 'USA')  # 安全访问，键不存在时返回默认值 'USA'
dict_keys = my_dict.keys()  # 获取所有键 (结果: dict_keys(['name', 'age', 'city']))
dict_values = my_dict.values()  # 获取所有值 (结果: dict_values(['Alice', 25, 'New York']))
dict_items = my_dict.items()  # 获取所有键值对 (结果: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')]))
dict_len = len(my_dict) # 长度 (结果: 3)

# 字典的修改、添加与移除 (字典是可变类型)
my_dict['age'] = 26  # 修改现有键的值 (my_dict: {'name': 'Alice', 'age': 26, 'city': 'New York'})
my_dict['email'] = 'alice@example.com'  # 添加新的键值对 (my_dict: {'name': 'Alice', ..., 'email': '...'})
dict_pop_value = my_dict.pop('city')  # 移除并返回指定键的值 (返回: 'New York', my_dict: {'name': 'Alice', 'age': 26, 'email': '...'})
my_dict.update({'age': 27, 'zip': 10001})  # 合并/更新字典 (my_dict: {'name': 'Alice', 'age': 27, 'email': '...', 'zip': 10001})
my_dict.clear() # 清空字典 (my_dict: {})

# 字典的常见错误
temp_dict = {'a': 1, 'b': 2}
# print(temp_dict['c'])                 # 错误：KeyError: 'c' (尝试访问不存在的键)
# temp_dict[{1, 2}] = 'value'           # 错误：TypeError: unhashable type: 'set' (字典的键必须是不可变类型，如字符串、数字、元组)
# temp_dict[[1, 2]] = 'value'           # 错误：TypeError: unhashable type: 'list' (列表是可变类型，不能作为键)
# print(temp_dict.pop('d'))             # 错误：KeyError: 'd' (pop移除不存在的键，且未提供默认值)




