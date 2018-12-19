# author:Bobby Chen

#导入模块
import matplotlib.pyplot as plt
from random import choice

num_points = 1000  # 生产随机漫步方向次数
x_value = [0]  # 初始点默认为（0,0）
y_value = [0]

while num_points:
    x_direction = choice([-1,1])  # 每次的移动方向
    x_distance = choice([-1,0,1])  # 每次朝移动方向的移动距离
    x_step = x_direction * x_distance  # 每次x方向移动的偏移量

    y_direction = choice([-1, 1])  # 每次的移动方向
    y_distance = choice([-1, 0, 1])  # 每次朝移动方向的移动距离
    y_step = y_direction * y_distance  # 每次y方向移动的偏移量

    #判断是否原地踏步
    if x_step == 0 and y_step ==0:
        continue


    #计算下一个点
    next_x = x_value[-1] + x_step
    next_y = y_value[-1] + y_step
    # 添加到列表
    x_value.append(next_x)
    y_value.append(next_y)
    # print(num_points)
    num_points -= 1

# 绘制得到的随机漫步散点图
plt.scatter(x_value,y_value,s=15,color="blue")
plt.title("RodomWalk Graph")
plt.show()