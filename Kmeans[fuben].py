# author:Bobby Chen

# 导入模块
import numpy as np
from sklearn.datasets import load_iris  # 加载IRIS数据集
import random
import matplotlib.pyplot as plt

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

def creat_clusters(Another_point,K_point):
    """对样本点测量其到每个质心的距离，把它归到最近的类"""
    dis_exchange= [99999999,0]
    # for Another_point in N:
    for point in K_point:
        dis_between_Kpoint = calculation_distance(Another_point, point[0])  # 计算样本点与每一个质心的距离
        if dis_between_Kpoint <= dis_exchange[0]:  # 取最小距离分类
            dis_exchange[0] = dis_between_Kpoint
            dis_exchange[1] = point[0]  #取标签
    return dis_exchange[1]  #返回这个样本点归类标签

def get_Kdiffirent_point(N,K,Labels):
    """生成K个随机索引,对于K个质心"""
    try:
        for n in range(2):
            random_index = random.sample(range(0, N.shape[0]), K)  # 尝试生成K个随机索引,对于K个不同类别的质心
            calss_Label = [Labels[i] for i in random_index]
            if len(calss_Label) == len(set(calss_Label)):  # 判断是否有重复类别质心
                break
            elif n == 1:  # 如果找不到K个不同类别的质心，抛出异常并处理
                raise Exception
    except Exception as ret:
        random_index = random.sample(range(0, N.shape[0]), K)
    finally:
        return random_index

def get_former_and_new_point(K_point,new_K_point):
    """得到新旧质心"""
    former_centriods = []
    New_centriods = []
    for i in K_point:
        former_centriods.append(np.array(i[:][0]))
    print("前一个质心", former_centriods)
    for i in new_K_point:
        New_centriods.append(np.array(i[:][0]))
    print("后一个质心：", New_centriods)
    former_centriods = np.array(former_centriods)
    New_centriods = np.array(New_centriods)
    return former_centriods,New_centriods

def recent_calssfiy(K,N,K_point):
    """对剩余的每个文档测量其到每个质心的距离，把它归到最近的类"""
    cluster = [i*[] for i in range(K)]  # 创建list根据标签存储不同类别的样本

    for index, i in enumerate(K_point):  # 把原来的几个质心分别装入列表作为不同类别标签
        cluster[index].append(i)

    for Another_point in N:
        classlabel = creat_clusters(Another_point, K_point)  # 获取每个样本分类后的标签
        for i in cluster:
            if classlabel in i[0]:
                i.append(Another_point)  # 将该样本放入最近的类别中
    return cluster

def K_Clustering(N,K,Labels):
    """K聚类分类器"""
    # 1. 从N个点随机选取K个点（K个类别）作为质心
    random_index = get_Kdiffirent_point(N,K,Labels)  # 生成K个随机索引,对于K个不同类别的质心
    K_point =[]
    for i in random_index:
        K_point.append([N[i],Labels[i]]) # N[i]对应的类标签Lables[i]
    print("初始质心",K_point)

    # 2. 对剩余的每个文档测量其到每个质心的距离，把它归到最近的类
    max_interations = 100000  #最大迭代次数
    for i in range(max_interations):
        cluster = recent_calssfiy(K,N, K_point)
        print(cluster)
        c=[]
        for i in cluster:
            c.append(i[0])
        # 3. 重新计算已经得到的各个类的质心
        new_K_point = []
        for i in cluster:
            print(i)
            new_center = list((np.array(i[1]).sum(axis=0))/len(np.array(i[1])))
            new_K_point.append([new_center,i[0]])
        print("-----------分割线-----------")
        print('新质心以及其类别标签：',new_K_point)

        # 4. 迭代23步直至新的质心与原质心相等或者小于指定的距离
        varepsilon = 0.0001  #收敛精度
        former_centriods, New_centriods = get_former_and_new_point(K_point,new_K_point)
        try:  # 在K值不等于类别种类数时，会出现维度不匹配的情况
            diff = New_centriods - former_centriods  # 计算新质心与原来质心的变化
        except:
            diff = np.array(0)
            pass
        if diff.all() < varepsilon:  # 判断是否达到收敛条件
            break
        else:
            K_point = new_K_point
            continue
    return cluster,New_centriods

def get_xy(data):
    """获取特征作为绘图坐标"""
    X = data[:, :1]  # 取第一列，即sepal_length
    Y = data[:, 1:2]  # 取第二列，即sepal_width
    return X,Y

def showCluster(K,classfiyresult,centroids):
    """数据可视化"""
    fig = plt.figure()
    plt.title("K-means classify Iris")
    ax = fig.add_subplot(111)
    data = []

    for i in range(K):  # 提取每个簇的数据
        ptsInClust = classfiyresult[i]
        data.append(ptsInClust)

    for i, color , marker in zip(range(K),["r","g","b"], ["+", "o", "*"]):
        x, y = get_xy(np.array(data[i]))
        ax.scatter(x, y, s = 40,c=color,marker=marker)

    centroidsx , centroidsy = get_xy(centroids)
    ax.scatter(centroidsx, centroidsy,s=100,c = "black",marker="+",alpha=1)  # 质心
    ax.set_xlabel("sepal_length")
    ax.set_ylabel("sepal_width")
    plt.show()


def main():
    """主函数：调用Kmeans聚类器以及调用可视化"""
    classfiyresult, centroids = K_Clustering(X,3,Y)  # Kmeans聚类,返回分类结果和质心
    # print("分类结果:\n","0:",classfiyresult[0],"\n","1:",classfiyresult[1],"\n","2:",classfiyresult[2])
    showCluster(3, classfiyresult, centroids)  # 可视化


if __name__ == '__main__':
    main()