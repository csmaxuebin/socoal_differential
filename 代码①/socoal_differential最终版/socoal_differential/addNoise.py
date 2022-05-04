import numpy as np
import pandas as pd
import binGroupingDensityCopy
import project
from exponent import exponent
import nodeStrength
import Grouping
import matplotlib.pyplot as plt
import time
import CDF

def addNoise(epsilon_exponet,epsilon_addnoise,date_pd_unproject):
    
    print(time.asctime(time.localtime(time.time())))
    print("-------------------------------------------------------")
    unproject_dataframe = pd.read_csv(date_pd_unproject)#读取文件
    # selectResult=exponent(epsilon_exponet,epsilon_addnoise,unproject_dataframe)#获得指数机制选择结果
    selectResult=[21, 36, 21, -326.66216216216174]
    print("selectResult--------------------------------------------")
    print(selectResult)
    centerNumber=selectResult[0]
    nodeDegreeThreshold=selectResult[1]
    edgeWeightThreshold=selectResult[2]
    project_dataframe = project.project(unproject_dataframe,nodeDegreeThreshold,edgeWeightThreshold)#投影
    nodeStrengthDic = nodeStrength.obtainNodeStrength(project_dataframe) # 获得节点强度字典
    center=binGroupingDensityCopy.searchCenterPoint(binGroupingDensityCopy.obtainDensity(nodeStrengthDic),centerNumber)#获得分组中心
    nodeStrengthDicTure = nodeStrength.obtainNodeStrength(unproject_dataframe)


    # print("project-noAddNoise------------------------------------------------")
    # NoAddnodeStrengthDic=nodeStrengthDic
    # print(NoAddnodeStrengthDic)
    NoAddCDFnodeStrengthDic=CDF.CDF(nodeStrengthDic)
    # print(nodeStrengthDic.values())

    groupingResult=Grouping.divide(center,nodeStrengthDic)#获得分组结果，然后将相同组内的bin 用均值代替
        #用平均值代替组内的bin的真实值，这一步还没添加噪音
    for i in groupingResult:
        sum=0
        for j in i:
            sum=sum+nodeStrengthDic[j]
        average=sum/len(i)#获得平均值
        for j in i:
            nodeStrengthDic[j]=average+np.random.laplace(0.0,(2*nodeDegreeThreshold+1)/(epsilon_addnoise*len(i)),1)
    for i in nodeStrengthDic:
        if nodeStrengthDic[i]<0:
            nodeStrengthDic[i]=0

    CDFnodeStrengthDic=CDF.CDF(nodeStrengthDic)


    # print("project-addNoise------------------------------------------")
    # print(nodeStrengthDic)
    # print("center------------------------------------------------------")
    # print(center)
    # print("groupingResult---------------------------------------------")
    # print(groupingResult)
    # # print("ture***************************************************")
    # # print(nodeStrengthDicTure)
    # print("CDFnodeStrengthDic,NoAddCDFnodeStrengthDic---------------------------------------------")
    # print(CDFnodeStrengthDic,NoAddCDFnodeStrengthDic)
    print("KSdistance---------------------------------------------")
    print(CDF.KsDistance(CDFnodeStrengthDic,NoAddCDFnodeStrengthDic))
    print("L1distance---------------------------------------------")
    NoAddnodeStrengthDic = nodeStrength.obtainNodeStrength(project_dataframe)
    print(CDF.L1Error(nodeStrengthDic,NoAddnodeStrengthDic))
    # print(nodeStrengthDic,NoAddnodeStrengthDic)
    print("end-----------------------------------------------------")
    print(time.asctime(time.localtime(time.time())))

epsilon=0.5
epsilon_exponet=0.2*epsilon
epsilon_addnoise=0.8*epsilon

for i in range(0,10):
    addNoise(epsilon_exponet,epsilon_addnoise,"soc-sign-bitcoinotc-Pretreatment.csv")

# addNoise(epsilon_exponet,epsilon_addnoise,"soc-sign-bitcoinotc-Pretreatment.csv")
