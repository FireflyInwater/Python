# author:Bobby Chen

# 导入模块
import numpy as np
from sklearn.datasets import load_iris  # 加载IRIS数据集
import operator
import random

# 导入数据集
iris = load_iris()
X = iris.data  # 特征向量，顺序排列150
Y = iris.target  # 标签

def calculation_distance(a,b):
    """计算两点之间的欧式距离"""
    distance = 0
    for index,n in enumerate(a):  # 对任意数量的特征量进行计算
        distance += (a[index]-b[index])**2
    distance = distance**0.5  # 得到两点的欧式距离
    return distance

def classify(test_data,dataSet,labels,k):
    """KNN分类器"""
    # 1.计算已知类别数据集中的点与当前点之间的距离；
    Distance = []  # 空列表存储距离
    for data in dataSet:
        Distance.append(calculation_distance(test_data, data))

    # 2.按照距离递增次序排序；
    Distance = np.array(Distance)
    sortedDisIndices = Distance.argsort()  # 返回Distance中元素从大到小排序后的索引

    # 3.选取与当前点距离最小的k个点；
    classCount = {}  # 计算次数
    for i in range(k):
        # 取前k个元素的类别
        vote_label = labels[sortedDisIndices[i]]

        # 4.确定前k个点所在类别的出现频率；
        classCount[vote_label] = classCount.get(vote_label, 0) + 1

    # 5.返回前k个点所出现频率最高的类别作为当前点的预测分类。
    sortedclassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedclassCount[0][0]

def main():
    """将整个样本随机取出百分之20的测试集，判断分类正确率"""

    test_percent = 0.20  # 测试比率
    length = X.shape[0]  # 数据集长度
    num_test = int(test_percent * length)  # 测试集个数
    # 分类错误率
    errorCount = 0.0

    # 生成随机索引列表，取测试样本
    random_index = random.sample(range(0,length),num_test)
    # print(random_index)
    # 定义测试集
    test_data = []
    test_label = []
    for i in random_index:
        test_data.append(X[i])
        test_label.append(i)
    # print(test_data)

    # 对每个样本进行分类
    for i in range(num_test):
        test_result=classify(test_data[i],X,Y,4)  # k取4
        print("样本数据：%s\t分类结果：%d\t真实类别：%d" %(str(test_data[i]),test_result, Y[test_label[i]]))
        if test_result != Y[test_label[i]]:
            errorCount += 1.0

    print("错误率：%f%%" % (errorCount/float(num_test)*100))


if __name__ == '__main__':
    main()