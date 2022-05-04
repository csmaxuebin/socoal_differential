import math

import networkx as nx
import csv
import random
import pandas as pd
import numpy as np
from Laplace import laplace_mech
import pickle

from tool_2 import random_choices_node


class OriginalWeightGraph_2:
    def __init__(self, fileName,epsilon):
        self.fileName = fileName #原始文件名字
        self.epsilon=epsilon #隐私预算
        self.originalGraph=self.get_orginal_graph()  #没有加噪没有投影的图
        self.degreeThreshold=self.get_degreeThreshold() #度的阈值
        self.proGraph=self.project_degree()
        self.degreeList=self.degree_list()
        self.NoiseGraph=self.get_NoiseGraph()
    def degree_list(self):
        degreeList=[]
        for i in self.proGraph:
            degreeList.append(self.proGraph.degree(i))
        print(degreeList)
        degreeList=laplace_mech(degreeList,2*self.degreeThreshold+1,self.epsilon)
        return degreeList
    #获得最原始的图
    def get_orginal_graph(self):
        graph_type = nx.Graph()
        csv_file = open(self.fileName)  # 打开原始csv文件
        csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
        edge_list = []
        for edge in csv_reader_lines:  # 逐行添加边到edge_list中
            edge_list.append([int(edge[0]), int(edge[1]), int(edge[2])])  # 添加图里面
        graph_type.add_weighted_edges_from(edge_list)  # 添加边到图中
        return graph_type
    #获得图的阈值
    def get_degreeThreshold(self):
        original_degree=nx.degree_histogram(self.originalGraph)
        count=0
        for i in range(0,len(original_degree)):
            if original_degree[i] ==0 :
                count+=1
            else:
                count=0
            if count==50:
                count=i
                break
        if count==0:
            count=len(original_degree)
        return count
    #根据图的度阈值对图进行投影,获得名字叫projectFilename的图
    def project_degree(self):
        for i in self.originalGraph.nodes():
            while self.originalGraph.degree(i)>self.degreeThreshold:#如果i节点的三角计数大于三角阈值
                j=find_min_triangle_node(i,self.originalGraph)
                self.originalGraph.remove_edge(i,j)
        return self.originalGraph
    def get_NoiseGraph(self):
        graph_type = nx.Graph()
        count=0
        for i in self.proGraph.nodes():
            graph_type.add_node(i, noiseDegree=self.degreeList[count])
            count=count+1
        while len(graph_type.edges())<len(self.proGraph.edges()):
            node =random_choices_node(graph_type, 2)
            i=node[0]
            j=node[1]
            degree_i = nx.get_node_attributes(graph_type, 'noiseDegree')[i]
            degree_j = nx.get_node_attributes(graph_type, 'noiseDegree')[j]
            weight = random.randint(0,10)
            if (i,j) not in graph_type.edges() \
                    and degree_j > graph_type.degree(j) \
                    and degree_i > graph_type.degree(i) :
                graph_type.add_edge(i, j, weight=weight)
                print("添加（"+str(i)+","+str(j)+")初始~~~~~~~~~~~~")
        return graph_type
