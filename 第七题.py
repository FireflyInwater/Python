# author:Bobby Chen
# -*- Coding:utf-8 -*-

#导入模块
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(12)  # x范围0-11
y1 = np.random.uniform(0,1,12)  # 生成12个0到1的随机数
y2 = np.random.uniform(0,1,12)
a=plt.bar(x,y1,color="lightskyblue")  # 绘制柱状图上部分
b=plt.bar(x,-y2,color="yellowgreen")  # 绘制柱状图下部分

# 使用text显示数值
for a, b in zip(x,y1):
    plt.text(a,b+0.05,"%.2f"%b,ha="center",va="bottom",fontsize=8)  # 添加数值显示，水平垂直居中
for a, b in zip(x,y2):
    plt.text(a,-(b+0.05),"%.2f"%b,ha="center",va="bottom",fontsize=8)

plt.title("The seven question.")
plt.axis("off")  # 消除坐标轴
plt.xticks([])  # 消除刻度线
plt.yticks([])
plt.show()
