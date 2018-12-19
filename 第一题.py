# author:Bobby Chen

#导入模块
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2,0.001)  # x范围 0-2 取步长0.001
y = ((np.sin(x-2))**2) * (np.exp(-x**2)) #  fx

# 绘制图像
# 定义图像窗口
plt.figure()
# 指定线条名称
plt.plot(x,y,label = "line_chenxiangbo")

# 设置坐标轴名称
plt.xlabel("x轴")
plt.ylabel("y轴")

# 设置标题
plt.title("The First Question Graph")
plt.legend()
plt.grid()  #生成网格
plt.show()
