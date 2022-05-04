import math

import networkx as nx
import csv
import pandas as pd
import numpy as np
from Laplace import laplace_mech
from tool import triangle_count_histogram, node_triangle_count, find_min_triangle_node, find_max_triangle_node
import pickle

class OriginalWeightGraph_2:
    def __init__(self, fileName):
        self.fileName = fileName #原始文件名字
        self.originalGraph=self.get_orginal_graph()  #没有加噪没有投影的图
    #获得最原始的图
    def get_orginal_graph(self):
        graph_type = nx.Graph()
        csv_file = open(self.fileName)  # 打开原始csv文件
        csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
        edge_list = []
        for edge in csv_reader_lines:  # 逐行添加边到edge_list中
            edge_list.append([int(edge[0]), int(edge[1])])  # 添加图里面
        graph_type.add_edges_from(edge_list)  # 添加边到图中
        return graph_type
test=OriginalWeightGraph_2("data/lastfm_asia_edges.csv")
list=list(test.originalGraph.edges)
print(type(list))
print(list)
name=["input","out"]
df=pd.DataFrame(list,columns=name)
df.to_csv(r'data/lastfm_asia_edges-pre.csv',encoding="gbk",index=False)
print(df)