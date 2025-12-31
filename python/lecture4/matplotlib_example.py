import matplotlib.pyplot as plt
import numpy as np

"""
准备数据
"""
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

"""
创建图像
"""
# 设置窗口大小
plt.figure(figsize=(8, 5))

"""
添加图像
可以调整格式，标签，线段粗细
"""
plt.plot(x, y1, label='Sine Wave', color='blue', linestyle='-', linewidth=2)
plt.plot(x, y2, label='Cosine Wave', color='red', linestyle='--', linewidth=2)

"""
坐标轴及图像标签
"""

#将图像标题设置为Trigonometric Functions
plt.title('Trigonometric Functions', fontsize=14)

#将x坐标轴设置为Time (s)
plt.xlabel('Time (s)')

#将y坐标轴设置为Amplitude
plt.ylabel('Amplitude')

#添加网格线
plt.grid(True, linestyle=':', alpha=0.6)

#将图像标签加入到图像中（自动寻找位置摆放）
plt.legend()

#显示图像
plt.show()