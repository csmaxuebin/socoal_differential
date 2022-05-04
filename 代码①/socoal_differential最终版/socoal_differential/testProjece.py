import qualityFunction
import math
import time
import pandas as pd
import binGroupingDensity
import project
import nodeStrength
import Grouping
def exponent(epsilon,unproject_dataframe):#参数是文件名
    # unproject_dataframe=pd.read_csv(date_pd_unproject)#投影之前的dataframe
    qualityScore=[]
    print(time.asctime(time.localtime(time.time())))
    print("*************************")
    for nodeDegreeThreshold in range(150,152):
        project_dataframe = project.project(unproject_dataframe, nodeDegreeThreshold,22)
        
        for edgeWeightThreshold in range(21,15,-1):
            project_dataframe=project.edgeProject(project_dataframe,edgeWeightThreshold)

            
            nodeStrengthDic=nodeStrength.obtainNodeStrength(project_dataframe)#5s
            
            
            projectError=2*qualityFunction.projectLoss(unproject_dataframe,nodeDegreeThreshold,edgeWeightThreshold)
            #3s
            print(time.asctime(time.localtime(time.time())))
            print("*************************")
            density=binGroupingDensity.obtainDensity(nodeStrengthDic)
            #10min
            print(time.asctime(time.localtime(time.time())))
            print("*************************")
            for centerNumber in range(10,100):
                groupcenter=binGroupingDensity.searchCenterPoint(density,centerNumber)
                groupResult=Grouping.divide(groupcenter,nodeStrengthDic)
                aggnoiseError=qualityFunction.aggregationErrorNoiseError(groupResult,
                                                                         nodeStrengthDic,
                                                                         nodeDegreeThreshold,
                                                                         0.8)
                score=-(projectError+aggnoiseError)
                print("centerNumber, nodeDegreeThreshold, edgeWeightThreshold, score=",end='')
                print(centerNumber,nodeDegreeThreshold,edgeWeightThreshold,score)
                print("       ")
                qualityScore.append([centerNumber,nodeDegreeThreshold,edgeWeightThreshold,score])
    exponents_list=[]
    for i in range(0,len(qualityScore)):
        exponents_list.append(math.exp((200*epsilon)/(12*9+8)))
    # print(type(qualityScore[exponents_list.index(max(exponents_list))]))
    selectResult=qualityScore[exponents_list.index(max(exponents_list))]
    return selectResult


unproject_dataframe=pd.read_csv("soc-sign-bitcoinotc-Pretreatment.csv")
exponent(0.2,unproject_dataframe)#参数是文件名
