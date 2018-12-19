# author:Bobby Chen

#导入模块
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,15,5,20]

# 定义图像窗口
plt.figure()
#绘制折线图
plt.plot(x,y,label="Fruit line")

# 绘制散点图
plt.scatter(x[0],y[0],label="apples",color="blue",s=100,marker="o")
plt.scatter(x[1],y[1],label="oranges",color="orange",s=100,marker="o")
plt.scatter(x[2],y[2],label="lemons",color="g",s=100,marker="o")
plt.scatter(x[3],y[3],label="limes",color="r",s=100,marker="o")

# 绘制条形图
plt.bar(x[0],y[0])
plt.bar(x[1],y[1])
plt.bar(x[2],y[2])
plt.bar(x[3],y[3])

plt.legend()
plt.xlabel("Fruit")
plt.ylabel("Number")
plt.title("The number of Fruit")
plt.show()
