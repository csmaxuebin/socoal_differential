#coding=utf-8
import numpy as np
import pandas as pd
import binGroupingDensityCopy
import project
import RSExponent
import nodeStrength
import Grouping
import matplotlib.pyplot as plt
import time
import CDF
import scipy.stats as stats


def MaxDegree(data_pd):
    nodeNumber = max(data_pd['input'].max(), data_pd['out'].max())  # 获得节点个数
    nodeDegree = {}
    for i in range(1, nodeNumber + 1):  # 为每个节点的节点度设置为0
        nodeDegree[i] = 0
    for index, row in data_pd.iterrows():
        nodeDegree[row['input']] += 1
        nodeDegree[row['out']] += 1
    #print(max(zip(nodeDegree.values(), nodeDegree.keys())))
    maxDegree=max(zip(nodeDegree.values(), nodeDegree.keys()))[0]
    return maxDegree

def addNoise(epsilon_exponet,epsilon_addnoise,date_pd_unproject):
    
    print(time.asctime(time.localtime(time.time())))
    print("-------------------------------------------------------")
    unproject_dataframe = pd.read_csv(date_pd_unproject)#读取文件
    # unproject_dataframe=project.project(unproject_dataframe,800,21)
    maxDegree=MaxDegree(unproject_dataframe)
    print("maxDegree=MaxDegree(unproject_dataframe) is ok")
    # print(maxDegree)
    nodeStrengthDic=nodeStrength.obtainNodeStrength(unproject_dataframe)
    # sum=0
    # for i in nodeStrengthDic:
    #     print(i,nodeStrengthDic[i])
    #     sum=sum+nodeStrengthDic[i]
    # print(sum)
    print("nodeStrengthDic=nodeStrength.obtainNodeStrength(unproject_dataframe) is ok")
    selectResult=RSExponent.exponent(epsilon_exponet,epsilon_addnoise,nodeStrengthDic,maxDegree)#获得指数机制选择结果
    # selectResult=[7, 12, -1750.809710144924, [1, 10, 12, 13, 37, 77, 132]]
    print("selectResult--------------------------------------------")
    print(selectResult)
    centerNumber=selectResult[0]
    # print(nodeStrengthDic)
    center=selectResult[3]#获得分组中心
    nodeStrengthDicTure = nodeStrength.obtainNodeStrength(unproject_dataframe)
    groupingResult=Grouping.divide(nodeStrengthDic,center)#获得分组结果，然后将相同组内的bin 用均值代替
        #用平均值代替组内的bin的真实值，这一步还没添加噪音
    for i in groupingResult:
        sum=0
        for j in i:
            sum=sum+nodeStrengthDic[j]
        average=sum/len(i)#获得平均值
        for j in i:
            nodeStrengthDic[j]=average+np.random.laplace(0.0,(2*maxDegree+1)/(epsilon_addnoise*len(i)),1)
    for i in nodeStrengthDic:
        if nodeStrengthDic[i]<0:
            nodeStrengthDic[i]=0
    #给所缺位置补上0
    for i in range(len(nodeStrengthDic)+1,len(nodeStrengthDicTure)+1):
        nodeStrengthDic[i]=0
    nodeStrengthDicvalues=list(nodeStrengthDic.values())
    nodeStrengthDicTurevalues=list(nodeStrengthDicTure.values())
    print(stats.ks_2samp(nodeStrengthDicTurevalues,nodeStrengthDicvalues))
    
    print("L1distance---------------------------------------------")
    print(CDF.L1Error(nodeStrengthDic,nodeStrengthDicTure))
    print("end-----------------------------------------------------")
    print(time.asctime(time.localtime(time.time())))
for epsilon in [0.1,0.5,1.0,1.5,2.0]:
    epsilon_exponet=0.2*epsilon
    epsilon_addnoise=0.8*epsilon
 
    for i in range(0,2):
        print(epsilon)
        addNoise(epsilon_exponet,epsilon_addnoise,"soc-sign-bitcoinotc-Pretreatment.csv")