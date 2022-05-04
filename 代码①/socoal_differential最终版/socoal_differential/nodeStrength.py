#得到节点强度字典
import pandas as pd
import numpy as np

def obtainNodeStrength(project_dataframe):
    nodeSet=set()#节点集合
    for index, row in project_dataframe.iterrows():
        nodeSet.add(row['input'])
        nodeSet.add(row['out'])  # 获得节点个数节点个数就是集合长度。从0开始
    nodeStrengthDic = {}#节点强度字典得到的是 节点强度：等于节点强度的节点个数
    nodeStrengthList= []#节点强度
    for i in nodeSet:
        nodeStrength = project_dataframe[project_dataframe['input'] == i]['weight'].sum()+project_dataframe[project_dataframe['out']==i]['weight'].sum()  # 得到每个节点的节点强度
        nodeStrengthList.append(nodeStrength)#添加到List

    # strenghtSet=set()#节点强度集合
    # for i in nodeStrengthList:
    #     strenghtSet.add(i)#获得所有的节点强度数值
    for i in range(1,int(max(nodeStrengthList))+1):
        nodeStrengthDic[i] = 0
    for i in nodeStrengthList:
        nodeStrengthDic[i]=nodeStrengthDic[i]+1 #得到节点强度字典
    # print("nodeStrength is ok")
    return nodeStrengthDic

# unproject_dataframe = pd.read_csv("soc-sign-bitcoinotc-Pretreatment.csv")
# # project_dataframe=project.project(unproject_dataframe,44,21)    
# nodeStrengthDic=obtainNodeStrength(unproject_dataframe)
# print(nodeStrengthDic)