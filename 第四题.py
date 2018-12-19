# author:Bobby Chen

#导入模块
import numpy as np
import matplotlib.pyplot as plt

#定义x,y
x = np.arange(-np.pi,np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = x
# 定义图像窗口
plt.figure()

plt.subplot(2,1,1) # 绘制多个子图的第一个
plt.plot(x,y1,label="y=sin(x)")
# 设置坐标轴1名称
plt.xlabel("x轴")
plt.ylabel("y1")
plt.title("The Four Question Graph")
plt.subplot(2,1,2)  # 绘制多个子图的第二个
plt.plot(x,y2,label="y=cos(x)")
plt.plot(x,y3,label="y=tan(x)")
plt.plot(x,y4,label="y=x")

# 设置坐标轴名称
plt.xlabel("x轴")
plt.ylabel("y轴")
# 设置标题
plt.title("The Four Question Graph")
plt.legend()
plt.grid()  #生成网格
plt.show()


