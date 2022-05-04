import pandas as pd
import numpy as np
import nodeStrength
import project
import time
#字典按照value进行排序，获得前n个k值
def searchCenterPoint(gamma, n):
    ordgamma = np.flipud(np.argsort(gamma)) #gamma是密度，ordgamma是排序之后的序号
    result=[]
    for i in range(n):
        result.append(ordgamma[i]+1)
    return result

#获得分组密度排序 gamma各个bin的密度
def obtainDensity(nodeStrengthDic):
    #dc阈值，自己设置
    dc=30
    
    #这部分是采用基于密度的方式来获得分组中心
    distlist = []#bin之间的距离
    dist = np.zeros((len(nodeStrengthDic), len(nodeStrengthDic)))#没问题
    for i in range(len(nodeStrengthDic)-1):
        for j in range(i+1,len(nodeStrengthDic)):
            distance=abs(nodeStrengthDic[i+1]-nodeStrengthDic[j+1])
            dist[i,j]=distance
            dist[j,i]=distance
    '''dc是阈值，求得方式是这样的，distlist只是用来求dc
    sortdist = sorted(distlist)
	position = round(len(distlist) * percent / 100)
	dc = sortdist[position]'''  
    #计算局部密度
    rho = np.zeros(len(dist))#局部密度rho：有多少个dist(i,j)>dc  i不变
    for i in range(len(dist)):
        for j in range(len(dist)):
            if(i!=j and dist[i,j]>dc ):
                rho[i]=rho[i]+1
    rho = [item / max(rho) for item in rho]  #局部密度按照比例投影到（0,1）中间
    ordrho = np.flipud(np.argsort(rho))#相当于将局部密度从大到小排列，提取索引输出
    #argsort()函数是将x中的元素从小到大排列，提取其对应的index(索引)，然后输出到y
    '''a=[1,2,3,4,1,3,2,0]
        print(np.flipud(a))
        结果：[0 2 3 1 4 3 2 1]
        '''
    # 生成 delta 和 nneigh 数组
	# nneigh 比本身密度大的最近的点
	# 记录 rho 值更大的数据点中与 ordrho(ii) 距离最近的点的编号 ordrho(jj)
	# 将 rho 按降序排列，ordrho 保持序
    delta=np.zeros(len(dist)) # delta 距离数组
    nneigh=np.zeros(len(dist),dtype=int)
    delta[ordrho[0]]=-1       #局部密度最大的距离为-1
    nneigh[ordrho[0]]=0       #局部密度最大点比自己大的最近的点是0
    maxd=max(dist.flatten())  # 求最大距离   #把dist按照行降维度
    for ii in range(1,len(dist)):
        delta[ordrho[ii]]=maxd #首先将所有的 最大距离 设置为最大值
        for jj in range(ii):
            if dist[ordrho[ii],ordrho[jj]]<delta[ordrho[ii]]:
                delta[ordrho[ii]]=dist[ordrho[ii],ordrho[jj]]
                nneigh[ordrho[ii]]=ordrho[jj]
        delta[ordrho[0]]=max(delta)
    gamma=[rho[i]*delta[i] for i in range (len(dist))]
    # gamma=np.array(gamma)
    return gamma
    
# unproject_dataframe = pd.read_csv("soc-sign-bitcoinotc-Pretreatment.csv")
# project_dataframe=project.project(unproject_dataframe,44,21)    
# nodeStrengthDic=nodeStrength.obtainNodeStrength(project_dataframe)
# print(nodeStrengthDic)
# gamma=obtainDensity(nodeStrengthDic)
# print(gamma)
# result = searchCenterPoint(gamma,5)
# print(result)