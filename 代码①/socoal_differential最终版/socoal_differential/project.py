import pandas as pd
import time


# 投影方法，参数就是dataframe类型的数据
import nodeStrength


def project(data_pd,nodeDegreeThreshold,edgeWeightThreshold):
    nodeNumber = max(data_pd['input'].max(), data_pd['out'].max())  # 获得节点个数
    nodeDegree = {}
    for i in range(1, nodeNumber + 1):  # 为每个节点的节点度设置为0
        nodeDegree[i] = 0
    data_pd=data_pd.sort_values(by="weight", ascending=True)
    for index, row in data_pd.iterrows():
        if ((nodeDegree[row['input']] < nodeDegreeThreshold) & (nodeDegree[row['out']] < nodeDegreeThreshold)):
            if (row['weight'] <= edgeWeightThreshold):  # 直接添加
                nodeDegree[row['input']] += 1
                nodeDegree[row['out']] += 1
            elif (row['weight'] > edgeWeightThreshold):  # 边权值改变，之后再添加
                nodeDegree[row['input']] += 1
                nodeDegree[row['out']] += 1
                data_pd.at[index, 'weight'] = edgeWeightThreshold
        else:  # 直接删除这条边
            # print("nodedegree=", end='')
            # print(nodeDegree[row['input']],nodeDegree[row['out']])
            data_pd.drop(index, inplace=True)
    return data_pd

def edgeProject(data_pd,edgeWeightThreshold):
    for index, row in data_pd.iterrows():
        if(row['weight'] > edgeWeightThreshold):  # 边权值改变，之后再添加
                data_pd.at[index, 'weight'] = edgeWeightThreshold
    return data_pd

# t1=time.time()
# dp=pd.read_csv("testPretreatment.csv")
# t2=time.time()
# print(t2-t1)
# print("**")
# data=project(dp,11,20)
# print(data)
# print("**")
# data1=edgeProject(data,10)
# print(data)
