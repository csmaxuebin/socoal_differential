import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

data = pd.read_csv("socTestOrigin.csv")
data_pd = pd.read_csv("socTestOriginPretreatment.csv")
nodeSet=set()#节点集合
for index, row in data.iterrows():
    nodeSet.add(row['input'])
    nodeSet.add(row['out'])  # 获得节点个数节点个数就是集合长度。从0开始
nodeStrengthDic = {}#节点强度字典得到的是 节点1：节点强度 节点2：节点强度
nodeStrengthList= []
for i in nodeSet:
    nodeStrength = data_pd[data_pd['input'] == i]['weight'].sum()+data_pd[data_pd['out']==i]['weight'].sum()  # 得到每个节点的节点强度
    nodeStrengthList.append(nodeStrength)
    nodeStrengthDic[i] = nodeStrength
print(nodeSet)
print("--------------")
print(nodeStrengthDic)
print(min(nodeStrengthList), max(nodeStrengthList))
bins = np.linspace(min(nodeStrengthList), max(nodeStrengthList), max(nodeStrengthList) - min(nodeStrengthList))
n, bins, patches = pl.hist(nodeStrengthList, bins)

pl.xlabel('nodeStrength')
pl.ylabel('nodeStrengthCount')
pl.title('nodeStrength')
pl.show()
