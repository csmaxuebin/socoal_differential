#coding=utf-8
import qualityFunction
import math
import time
import pandas as pd

import project
import nodeStrength
import Grouping
import binGroupingDensityCopy
import Randomly
import random 

def random_pick(some_list, probabilities): 
    x = random.uniform(0,1) 
    cumulative_probability = 0.0 
    for item, item_probability in zip(some_list, probabilities): 
         cumulative_probability += item_probability 
         if x < cumulative_probability:
               break 
    return item

def exponent(epsilon_exponet,epsilon_addnoise,nodeStrengthDic,maxDegree):#参数是文件名
    qualityScore=[]
    for centerNumber in range(20,21):
        result=Randomly.divideReplace(nodeStrengthDic,centerNumber,maxDegree,epsilon_addnoise)
        aggnoiseError=result[0]
        center=result[1]
        score=-(aggnoiseError)
        #print("centerNumber,nodeDegreeThreshold,score,center====",end='')
        #print(centerNumber,maxDegree,score,center)
        qualityScore.append([centerNumber,maxDegree,score,center])
    exponents_list=[]
 
    for i in range(0,len(qualityScore)):
        exponents_list.append(math.exp((qualityScore[i][2]*epsilon_exponet)/(2*(6*100+4))))
    exponents_list_sum=sum(exponents_list)
    exponents_list_sumlist=[]
    for i in range(0,len(exponents_list)):
        exponents_list_sumlist.append(exponents_list[i]/exponents_list_sum)
    selectResult=random_pick(qualityScore,exponents_list_sumlist) 
    return selectResult

