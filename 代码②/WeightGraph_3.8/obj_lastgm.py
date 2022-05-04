import pickle
import networkx as nx

import time

from OriginalWeightGraph_2 import OriginalWeightGraph_2
from tool_2 import *
import matplotlib.pyplot as plt
import scipy.stats as stats
original = OriginalWeightGraph_2("data/lastfm_asia_edges.csv",0.1)
original_1=pickle.dumps(original)
with open("object/lastfm_asia_edges_0.1", "ab")as f:
    f.write(original_1)

#读取文件中的对象文件
#pickle.load()一次只读取一个对象文件
f=open("object/lastfm_asia_edges_0.1", "rb")
while 1:
    try:
        obj = pickle.load(f)
        print(obj.epsilon,obj)
        print(obj.triangleCountThreshold,obj)
        A=obj.degree_strength_triangleCount
        print(A)
    except:
            break
f.close()
