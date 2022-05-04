#coding=utf-8
#rho = [item / max(rho) for item in rho]  
def CDF(nodeStrengthDic): #累计节点强度分布
    CDFnodeStrengthDic={}
    CDFnodeStrengthList=[]
    for i in nodeStrengthDic:
        CDFnodeStrengthDic[i]=nodeStrengthDic[i]
        for j in range(1,i):
            CDFnodeStrengthDic[i]=CDFnodeStrengthDic[i]+ nodeStrengthDic[j]
    for i in CDFnodeStrengthDic:
        CDFnodeStrengthList.append(nodeStrengthDic[i])
    CDFnodeStrengthList= [item / sum(CDFnodeStrengthList) for item in CDFnodeStrengthList]

    for i in range(len(CDFnodeStrengthList)):
        CDFnodeStrengthDic[i+1]=CDFnodeStrengthList[i]
    return CDFnodeStrengthDic



def L1Error(nodeStrengthDic,NoAddnodeStrengthDic):
    l1error=0
    for i in range(1,len(nodeStrengthDic)):
        l1error=abs(nodeStrengthDic[i]-NoAddnodeStrengthDic[i])+l1error
    return l1error



