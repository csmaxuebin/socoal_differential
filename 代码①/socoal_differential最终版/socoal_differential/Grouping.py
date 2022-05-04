import nodeStrength
import pandas as pd
import numpy as np
import nodeStrength
import project
import time
import binGroupingDensityCopy
'''
参数：分组中心和节点强度字典
'''
def divide(center=[],nodeStrengthDic={}):
    groupingResult = []#划分结果
    center = sorted(center)#  分组中心排序
    for i in center:
        groupingResult.append([i])
    for i in nodeStrengthDic:
        if i not in center:
            if i <center[0]:           #如果i小于等于一个分组号，直接分进去
                groupingResult[0].append(i)
            elif i >center[len(center)-1]:
                groupingResult[len(center)-1].append(i) #如果大于等于一个分组号，直接分进去
    for j in range(0,len(center)-1): #每个分组中的数 找到一个合适点的数
        if center[j]+1 !=center[j+1]: #如果两个中心相邻就跳过
            minI=0
            minLeft=0 #左边误差
            minRight=0
            min=float("inf") #每个数的左右误差 
            for i in range(center[j]+1,center[j+1]): #遍历两个中心之间的数
                leftSum=0   #左边误差和
                for m in range(center[j]+1,i+1): #范围center[j]+1也就是 左中心后的数到i
                    leftSum=leftSum+abs(nodeStrengthDic[m]-nodeStrengthDic[center[j]])
                left=leftSum/(i-center[j]) #左边的误差
                rightSum = 0
                for m in range(i,center[j+1]): #范围是i 到右中心
                    rightSum = rightSum + abs(nodeStrengthDic[m] - nodeStrengthDic[center[j+1]])
                right = rightSum / (center[j+1]-i)
                sum=left+right #总和
                # print(i,sum,left,right)
                if sum<min:
                    min=sum
                    minI=i
                    minLeft=left
                    minRight=right
            if(minLeft<=minRight):
                for i in range(center[j]+1,minI+1): #如果左边的小于右边的 就把MinI分到左边
                    groupingResult[j].append(i)
                for i in range(minI+1,center[j+1]):
                    groupingResult[j+1].append(i)
            if(minLeft>minRight):                   #否则分到右边
                for i in range(center[j]+1,minI):
                    groupingResult[j].append(i)
                for i in range(minI,center[j+1]):
                    groupingResult[j+1].append(i)

            
            
            
           
    return groupingResult

# unproject_dataframe = pd.read_csv("soc-sign-bitcoinotc-Pretreatment.csv")
# project_dataframe=project.project(unproject_dataframe,44,21)    
# nodeStrengthDic=nodeStrength.obtainNodeStrength(project_dataframe)
# print(nodeStrengthDic)
# # gamma=binGroupingDensityCopy.obtainDensity(nodeStrengthDic)
# # print(gamma)
# # result = binGroupingDensityCopy.searchCenterPoint(gamma,5)
# # print(result)
# result=[1,7,14,15,37,50]
# groupingResult=divide(result,nodeStrengthDic)
# print(groupingResult)

