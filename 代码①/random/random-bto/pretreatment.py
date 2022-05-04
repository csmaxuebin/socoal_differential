import pandas as pd
import time
#对数据进行预处理 因为这特么是个有向图 好气哦
#输入时一个csv 文件 输出还是一个csv文件
#2.要将边的权值变为正数
# data_pd = pd.read_csv("testOrigin.csv")
def pretreatment(data_pd):
    print("开始：", end='')
    print(time.asctime(time.localtime(time.time())))
    minNodeStrength = data_pd['weight'].min()
    if (minNodeStrength < 0):
        for i in range(len(data_pd)):
             data_pd['weight'][i] = data_pd['weight'][i] +abs(minNodeStrength)+1
    print("ok")
        #1.要对边进行处理，如果一条边的出边等于入边，入边等于出边，则删除边
    for index1,row1 in data_pd.iterrows():
        print(time.asctime(time.localtime(time.time())))
        for index2,row2 in data_pd.iterrows():
            if (row1['input']==row2['out']) & (row2['input']==row1['out']):
                data_pd.drop(index2, inplace=True)
                print("delete")
    data_pd.to_csv(r'C:\Users\xiaojiu\Desktop\test\facebook-Pretreatment.csv',encoding="gbk",index=False)
    print("结束：", end='')
    print(time.asctime(time.localtime(time.time())))

pretreatment(pd.read_csv("facebook.csv"))