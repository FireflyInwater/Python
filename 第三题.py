# author:Bobby Chen

#导入模块
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #  导入三维空间绘图工具

# 定义绘图窗口对象
fig = plt.figure()
ax1 = Axes3D(fig)

x = np.arange(-4,4,0.01) # 定义xy范围
y = np.arange(-4,4,0.01)
#meshgrid函数通常使用在数据的矢量化上。
#它适用于生成网格型数据，可以接受两个一维数组生成两个二维矩阵，对应两个数组中所有的(x,y)对。
x,y = np.meshgrid(x,y)

r = np.sqrt(x**2+y**2)
z = np.sin(r)

ax1.plot_surface(x,y,z,rstride = 1,  # row行步长
                 cstride = 2,  # colum 列步长
                 cmap = plt.cm.hot)  # 渐变色

ax1.contourf(x,y,z,  # 绘制图形的等高线
             zdir="z", # 使用z方向
             offset=-2,  # 填充投影
             cmap=plt.cm.hot)
ax1.set_zlim(-2,2)
# # # 设置坐标轴名称
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")

# 设置标题
plt.title("The Third Question Graph")
plt.legend()
plt.show()