import numpy as np#导入numpy 库，标记为numpy
print(np.pi)#输出numpy库中的pi值




"""np ndarray/array:np的核心部分的构造"""
# 使用list构造ndarray
simple_arr = np.array([10, 20, 30])

# 创建2d array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
"""
创建由0和1所构成的矩阵
"""

#全是0的矩阵
zeros = np.zeros((2, 5))    #2*5的全0矩阵

#3*3单位对角矩阵
identity = np.eye(3)

#随机对角矩阵
random_vals = np.random.randint(0, 100, (3, 3)) # 3x3 matrix of random ints

print(f"Random Matrix:\n{random_vals}\n")


"""
ndarray的形状
"""
print("--- 2. Inspection ---")
#输出矩阵的形状
print(f"Shape: {matrix.shape}")  # (3, 3)

#输出存储矩阵数据类型
print(f"Data Type: {matrix.dtype}")  # int64 or int32
#输出矩阵的元素数量
print(f"Total Elements: {matrix.size}\n")


"""
ndarray的查找与slicing
"""

#查找
print("--- 3. Indexing & Slicing ---")
print(f"Element at Row 0, Col 1: {matrix[0, 1]}")

# Slicing
print(f"First two rows:\n{matrix[0:2, :]}")
print(f"The second column: {matrix[:, 1]}\n")


"""
加减
"""
print("--- 4. Vectorized Operations ---")
arr = np.array([1, 2, 3])

# 所有的运算都作用在每一个单独元素上
print(f"Add 10: {arr + 10}")
print(f"Square: {arr ** 2}")
print(f"Boolean Mask (val > 1): {arr > 1}\n")


"""
求和运算
"""

print("--- 5. Aggregations ---")
test_data = np.array([[1, 2], [3, 4]])

print(f"Total Sum: {np.sum(test_data)}")
print(f"Sum of each column: {np.sum(test_data, axis=0)}")
print(f"Max of each row: {np.max(test_data, axis=1)}\n")


"""
重组运算
"""
print("--- 6. Reshaping")
flat = np.arange(12)  # [0, 1, ..., 11]
reshaped = flat.reshape(3, 4) # Changes 1x12 into 3x4
print(f"Reshaped 3x4 Matrix:\n{reshaped}")

"""
基本线性代数运算
"""

arr1 = np.array([1,2,3])
arr2=np.array([4,5,6])

#向量叉积
res1=arr1@arr2
res2=np.dot(arr1,arr2)


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 使用 @ 符号进行矩阵乘法 (推荐)
C = A @ B
print(f"矩阵 A @ B:\n{C}")
print(f"矩阵 A 的转置:\n{A.T}")
print(f"矩阵 A 的行列式: {np.linalg.det(A):.2f}")
print("-" * 30)

print("===  求解线性方程组 (Ax = b) ===")
# 场景：2x + y = 8; x - 3y = -3
coeffs = np.array([[2, 1], [1, -3]])
dep_vars = np.array([8, -3])

# 使用 solve 而不是 inv，效率更高更稳定
solution = np.linalg.solve(coeffs, dep_vars)
print(f"方程组的解: x = {solution[0]}, y = {solution[1]}")
print("-" * 30)

print("===  特征值与特征向量 ===")
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"特征值: {eigenvalues}")
print(f"特征向量矩阵:\n{eigenvectors}")
print("-" * 30)

print("===  矩阵分解 (SVD) ===")
# SVD 分解将矩阵分解为 U, Sigma, V_transpose
U, s, Vh = np.linalg.svd(A)
print(f"奇异值 (Sigma): {s}")
print("-" * 30)

print("===  范数 (Norm) 与 秩 (Rank) ===")
print(f"A 的 Frobenious 范数: {np.linalg.norm(A)}")
print(f"A 的秩 (Rank): {np.linalg.matrix_rank(A)}")






