# author:Bobby Chen

#导入模块
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris  # 加载IRIS数据集

iris = load_iris()
X = iris.data  # 特征向量，顺序排列
Y = iris.target  # 标签
x = X[:,:1]  # 取第一列，即sepal_length
y = X[:,2:3]  # 取第三列，即petal_length

plt.scatter(x,y,c="r",marker="*")  # 选取花萼长度与花瓣长度绘制散点图
plt.xlabel("sepal_length")
plt.ylabel("petal_length")
plt.title("The relationship of sepal_length between petal_length")
plt.show()