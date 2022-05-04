#coding=utf-8
import nodeStrength
import project
import pandas as pd
import random
import Grouping
import qualityFunction
import operator
import copy

def randomlySelect(nodeStrengthDic,n):
    #第一步随机选择一个bin作为第一个中心，再选择离第一中心最远的bin作为第二个中心，
    # 第三个中心离第一个和第二个中心都是最远，…直到选择出k个中心
    list=range(1,len(nodeStrengthDic)+1)
    center=random.sample(list, n)
    return center

    
def divideReplace(nodeStrengthDic,centerNumber,nodeDegreeThreshold,epsilon_addnoise):
    randomlySelectCenter=randomlySelect(nodeStrengthDic,centerNumber)
    #随机选择出来的中心
    randomlySelectCenter.sort()
    # print("randomlySelectCenter")
    # print(randomlySelectCenter)
    #对中心进行排序
    # #按照中心进行划分
    bestGroupResult=Grouping.divide(nodeStrengthDic,randomlySelectCenter)
    # print(bestGroupResult)
    bestCenter=copy.deepcopy(randomlySelectCenter)
    bestAggnoiseError=qualityFunction.aggregationErrorNoiseError(bestGroupResult,nodeStrengthDic,nodeDegreeThreshold,epsilon_addnoise)
   
    #求得聚合噪音
    i=0
    while i<centerNumber:
        # print("i=============",end='')
        # print(i)
        temporaryCenter=copy.deepcopy(bestCenter)
        temporaryGroupResult=copy.deepcopy(bestGroupResult)
        for j in range(1,len(bestGroupResult[i])):#
            # print("j=",end='')
            # print(j)
            # print(temporaryCenter[i],bestGroupResult[i][j] )
            temporaryCenter[i]=bestGroupResult[i][j] #将暂时结果先赋值
            temporaryAggnoiseError=qualityFunction.aggregationErrorNoiseError(Grouping.divide(nodeStrengthDic,temporaryCenter),nodeStrengthDic,nodeDegreeThreshold,epsilon_addnoise)
            # print(temporaryAggnoiseError,bestAggnoiseError)
            if temporaryAggnoiseError<bestAggnoiseError:
                # print("*******")
                # print(temporaryAggnoiseError,bestAggnoiseError)
                # print(temporaryCenter,bestCenter)
                bestAggnoiseError=temporaryAggnoiseError
                bestCenter=copy.deepcopy(temporaryCenter)
                bestGroupResult=Grouping.divide(nodeStrengthDic,bestCenter)
                # print("!!!!!!")
                i=-1
                break
            # print(bestCenter)
            temporaryCenter=copy.deepcopy(bestCenter)
        i=i+1           
                   
    # temporaryGroupResult=bestCenter
    #     for i in range(0,len(temporaryGroupResult)):#有多少个组
    #         bestCenter=temporaryCenter#暂定最好的就是这个
    #         for j in range(1,len(temporaryGroupResult[i])):
    #             #替换，然后求聚合噪音，聚合噪音小的就替换，聚合噪音大就不替换
    #             temporaryCenter[i]=temporaryGroupResult[i][j]
    #             temporaryAggnoiseError=qualityFunction.aggregationErrorNoiseError(Grouping.divide(nodeStrengthDic,temporaryCenter),nodeStrengthDic,nodeDegreeThreshold,epsilon_addnoise)
    #             if temporaryAggnoiseError<bestAggnoiseError:
    
    #                 bestAggnoiseError=temporaryAggnoiseError
    #                 bestCenter=temporaryCenter
    #                 bestGroupResult=Grouping.divide(nodeStrengthDic,bestCenter)
    # temporaryGroupResult=bestCenter
    # print(bestCenter)
    # print(bestAggnoiseError)
    result=[]
    result.append(bestAggnoiseError)
    result.append(bestCenter)
    # print("result----------------------")
    # print(result)
    return result
#条件区域
# unproject_dataframe = pd.read_csv("soc-sign-bitcoinotc-Pretreatment.csv")
# project_dataframe=project.project(unproject_dataframe,100,21)
# nodeStrengthDic=nodeStrength.obtainNodeStrength(project_dataframe)
# # nodeStrengthDic={1: 223, 2: 62, 3: 15, 4: 5, 5: 4, 6: 21, 7: 13, 8: 11, 9: 19, 10: 85, 11: 13, 12: 802, 13: 190, 14: 93, 15: 51, 16: 61, 17: 13, 18: 20, 19: 20}
# print(nodeStrengthDic)
# divideReplace(nodeStrengthDic,20,100,2)