# author:Bobby Chen


#导入模块
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris  # 加载IRIS数据集

iris = load_iris()
X = iris.data  # 特征向量，顺序排列
Y = iris.target  # 标签

# print(type(X)) # 测试X类型
sepal_length = X[:,:1]  # 取第一列，即sepal_length
sepal_width = X[:,1:2]  #取第二列，即sepal_width
petal_length = X[:,2:3]  # 取第三列，即petal_length
petal_width = X[:,3:4]  # 取第四列，即petal_width

x = np.array(sepal_length) * np.array(sepal_width)  # 每个元素对应相乘计算size
y = np.array(petal_length) * np.array(petal_width)

plt.scatter(x,y,c="r",marker="*")  # 绘制花萼与花瓣大小关系的散点图
plt.xlabel("sepal_size")
plt.ylabel("petal_size")
plt.title("The relationship of sepal_size between petal_size")
plt.show()