# author:Bobby Chen

# 导入模块
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris  # 加载IRIS数据集

iris = load_iris()
X = iris.data  # 特征向量，顺序排列
Y = iris.target  # 标签

# 定义三个空列表用作存储三种花
Setosa = []
Versicolour = []
Virginica = []

# 将三个不同种类的花分类存储
for index, i in enumerate(Y):
    # print(index) index 为索引
    if i == 0:
        Setosa.append(list(X[index]))
    elif i == 1:
        Versicolour.append(list(X[index]))
    else:
        Virginica.append(list(X[index]))

Setosa = np.array(Setosa)  # 转化为数组形式
Versicolour = np.array(Versicolour)
Virginica = np.array(Virginica)
print("分类得到的Setosa类型花的数据集：", Setosa)
print("分类得到的Versicolour类型花的数据集：", Versicolour)
print("分类得到的Virginica类型花的数据集：", Virginica)


# 定义一个计算花萼与花瓣大小的函数
def get_size(a):
    sepal_length = a[:, :1]  # 取第一列，即sepal_length
    sepal_width = a[:, 1:2]  # 取第二列，即sepal_width
    petal_length = a[:, 2:3]  # 取第三列，即petal_length
    petal_width = a[:, 3:4]  # 取第四列，即petal_width
    x = np.array(sepal_length) * np.array(sepal_width)
    y = np.array(petal_length) * np.array(petal_width)
    return x, y


# 计算三种花的size
x1, y1 = get_size(Setosa)
x2, y2 = get_size(Versicolour)
x3, y3 = get_size(Virginica)

# 使用散点图绘制不同种类之间的花萼与花瓣的关系
plt.scatter(x1, y1, c="r", marker="*", label="Setosa")  # 绘制Setosa花萼与花瓣大小关系的散点图
plt.scatter(x2, y2, c="g", marker="o", label="Versicolour")  # 绘制Versicolour花萼与花瓣大小关系的散点图
plt.scatter(x3, y3, c="blue", marker="+", label="Virginica")  # 绘制Virginica花萼与花瓣大小关系的散点图

plt.xlabel("sepal_size")  # 坐标标识
plt.ylabel("petal_size")
plt.title("The relationship of sepal_size between petal_size")  # 标题
plt.legend()  # 显示图例
plt.show()
