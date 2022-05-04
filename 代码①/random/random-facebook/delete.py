#coding=utf-8
import pandas as pd
import time
from pandas.core.frame import DataFrame
def delete(data_pdA,data_pdB):
    print("开始：", end='')
    print(time.asctime(time.localtime(time.time())))
    listA=data_pdA.values.tolist()
    listB=data_pdA.values.tolist()
    deleteX=[x for x in listA if x in listB]
    print("OK")
    deleteA=[]
    for list in deleteX:
        if list[0]-list[1]>0:
            deleteA.append(list)
    print("OK")
    listC=[x for x in listA if x not in deleteA] #已经把重复的删除了
    print("OK")
    data_pdC = DataFrame(listC,columns=['input','out'])
    print("OK")
    data_pdC.to_csv(r'C:\Users\xiaojiu\Desktop\test\data_pdC.csv',encoding="gbk",index=False)
    print("OK,OVER")
    print(time.asctime(time.localtime(time.time())))
delete(pd.read_csv("Wiki-VoteA.csv"),pd.read_csv("Wiki-VoteB.csv"))
