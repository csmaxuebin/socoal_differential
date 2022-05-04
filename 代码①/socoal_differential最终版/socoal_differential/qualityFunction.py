#质量函数
#投影损失,找到有多少个节点发生了变化

import nodeStrength
import Grouping
import pandas as pd

def projectLoss(unproject_dataframe,nodeDegreeThreshold,edgeWeightThreshold):

    nodeSet=set()#节点集合
    nodeDegree={}#节点度的字典
    alterNode=set()#发生改变的节点集合
    for index, row in unproject_dataframe.iterrows():
        nodeSet.add(row['input'])
        nodeSet.add(row['out'])#获得节点个数节点个数就是集合长度。从0开始

    for i in nodeSet:
        nodeDegree[i] =0;                  #将节点度设置为0

    for index, row in unproject_dataframe.iterrows():
        nodeDegree[row['input']] = nodeDegree[row['input']] + 1
        nodeDegree[row['out']] = nodeDegree[row['out']] + 1
        if(row['weight']>edgeWeightThreshold):
            alterNode.add(row['input'])
            alterNode.add(row['out'])

    for i in nodeSet:
        if nodeDegree[i]>nodeDegreeThreshold:
            alterNode.add(i)
    return len(alterNode)



def aggregationErrorNoiseError(groupingResult,nodeStrengthDic,nodeDegreeThreshold,epsilon):
    # print("aggregationErrorNoiseError开始")
    # print("groupingResult",end='')
    # print(groupingResult)
    # print("nodeStrengthDic", end='')
    # print(nodeStrengthDic)
    for i in groupingResult:
        binSum=0
        for j in i:
            binSum =binSum+nodeStrengthDic[j]
        averageSum=binSum/len(i)
        totalError=0
        for j in i:
            aggregationError=abs(nodeStrengthDic[j]-averageSum)
            noiseError = ((2 * nodeDegreeThreshold) + 1) / (epsilon * len(i))
            totalError = aggregationError + noiseError+totalError
    #     print("i=",end='')
    #     print(i)
    #     print("aggregationError=", end='')
    #     print(aggregationError)
    #     print("noiseError=", end='')
    #     print(noiseError)
    # print("Error=", end='')
    # print(Error)
    # print("aggregationErrorNoiseError结束")


    '''
    projectError 8
    aggnoiseError 1.0116704161979753
    '''
    return totalError

