import qualityFunction
import math
import time
import pandas as pd

import project
import nodeStrength
import Grouping
import binGroupingDensityCopy
def exponent(epsilon_exponet,epsilon_addnoise,unproject_dataframe):#参数是文件名
    qualityScore=[]
    for nodeDegreeThreshold in range(20,150):
        project_dataframe = project.project(unproject_dataframe, nodeDegreeThreshold,22)
        for edgeWeightThreshold in range(21,20,-1):
            project_dataframe=project.edgeProject(project_dataframe,edgeWeightThreshold)
            nodeStrengthDic=nodeStrength.obtainNodeStrength(project_dataframe)
            projectError=2*qualityFunction.projectLoss(unproject_dataframe,nodeDegreeThreshold,edgeWeightThreshold)
            density=binGroupingDensityCopy.obtainDensity(nodeStrengthDic)
            for centerNumber in range(1,150):
                groupcenter=binGroupingDensityCopy.searchCenterPoint(density,centerNumber)
                groupResult=Grouping.divide(groupcenter,nodeStrengthDic)
                aggnoiseError=qualityFunction.aggregationErrorNoiseError(groupResult,
                                                                         nodeStrengthDic,
                                                                         nodeDegreeThreshold,
                                                                         epsilon_addnoise)
                score=-(projectError+aggnoiseError)
                # print("projectError")
                # print(projectError)
                # print("aggnoiseError")
                # print(aggnoiseError)
                print("centerNumber,nodeDegreeThreshold,edgeWeightThreshold,score")
                print(centerNumber,nodeDegreeThreshold,edgeWeightThreshold,score)
                qualityScore.append([centerNumber,nodeDegreeThreshold,edgeWeightThreshold,score])
    exponents_list=[]
    
    for i in range(0,len(qualityScore)):
        exponents_list.append(math.exp((qualityScore[i][3]*epsilon_exponet)/(2*(6*150+4))))

    selectResult=qualityScore[exponents_list.index(max(exponents_list))]
    return selectResult
