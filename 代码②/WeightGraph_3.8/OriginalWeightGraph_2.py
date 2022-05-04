import math

import networkx as nx
import csv
import pandas as pd
import numpy as np
from Laplace import laplace_mech
from tool_2 import triangle_count_histogram, node_triangle_count, find_min_triangle_node, find_max_triangle_node
import pickle

class OriginalWeightGraph_2:
    def __init__(self, fileName,epsilon):
        self.fileName = fileName #原始文件名字
        self.epsilon=epsilon #隐私预算
        self.originalGraph=self.get_orginal_graph()  #没有加噪没有投影的图
        self.degreeThreshold=self.get_degreeThreshold() #度的阈值
        # self.degreeThreshold=4 #度的阈值
        self.triangleCountThreshold=self.get_triangleCountThreshold()#三角计数的阈值
        # self.triangleCountThreshold=self.degreeThreshold/2
        self.projectGraph = self.get_project_graph()  # 得到节点属性有度和强度的图
        self.degree_strength_triangleCount = list(nx.get_node_attributes(self.projectGraph, 'degree_strength_triangleCount').values()) # 得到节点度和节点强度序列
        self.ds_frequency = self.getNodeFrequency()  # 得到[节点度，节点强度]的加噪频度统计
        self.weight_frequency = self.getWeightFrequency() # 得到权值的加噪频度统计
        self.edge_number=self.Edge_Number()
        self.triangleNumber=self.TriangleNumber()
    def Edge_Number(self):
        while True:
            zhenzhi=len(self.originalGraph.edges())
            edge_number=laplace_mech([zhenzhi], self.degreeThreshold, self.epsilon*0.1)[0]
            chazhi=zhenzhi-edge_number
            # print("边差值"+str(chazhi)+"，真值"+str(zhenzhi)+"，加噪值"+str(edge_number)+"，比值"+str(chazhi/zhenzhi))
            if chazhi/zhenzhi<0.3 and chazhi/zhenzhi>0:
                return edge_number
    def TriangleNumber(self):
        while True:
            zhenzhi=sum(nx.triangles(self.originalGraph).values())/3
            triangleNumber=laplace_mech([zhenzhi],self.triangleCountThreshold,0.1*self.epsilon)[0]
            chazhi=triangleNumber-zhenzhi
            # print("三角差值"+str(chazhi)+",真值"+str(zhenzhi)+",加噪值"+str(triangleNumber)+",比值"+str(chazhi/zhenzhi))
            if chazhi/zhenzhi<0.12 and  chazhi/zhenzhi>-0.12 :
                return triangleNumber
    #获得最原始的图
    def get_orginal_graph(self):
        graph_type = nx.Graph()
        csv_file = open(self.fileName)  # 打开原始csv文件
        csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
        edge_list = []
        for edge in csv_reader_lines:  # 逐行添加边到edge_list中
            edge_list.append([int(edge[0]), int(edge[1]), int(edge[2])])  # 添加图里面
        graph_type.add_weighted_edges_from(edge_list)  # 添加边到图中
        for n in graph_type.nodes():#遍历所有节点
            graph_type.add_node(n, triangle_count=nx.triangles(graph_type,n))
        # print("原始图[三角计数]已完成")
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
        print("get_degreeThreshold"+str(count))
        return count
    #获得三角计数的阈值
    def get_triangleCountThreshold(self):
        original_triangleCount=triangle_count_histogram(self.originalGraph)
        count=0
        for i in range(0,len(original_triangleCount)):
            if original_triangleCount[i] ==0 :
                count+=1
            else:
                count=0
            if count==10:
                count=i
                break
        if count==0:
            count=len(original_triangleCount)
        print("get_triangleCountThreshold"+str(count))
        return count
    #根据图的度阈值对图进行投影,获得名字叫projectFilename的图
    def project_degree(self,graph):
        for i in graph.nodes():
            while graph.degree(i)>self.degreeThreshold:#如果i节点的三角计数大于三角阈值
                j=find_min_triangle_node(i,graph)
                graph.remove_edge(i,j)
        return graph
    #根据图的三角阈值对图进行投影
    def project_triangle(self,graph):
        for i in graph.nodes():
            while node_triangle_count(i,graph)>self.triangleCountThreshold:#如果i节点的三角计数大于三角阈值
                j=find_max_triangle_node(i,graph)
                graph.remove_edge(i,j)
        return graph
    # 根据csv文件获得节点属性为[节点度，节点强度]的图
    def get_project_graph(self):
        graph_type = nx.Graph()
        data_pd=pd.read_csv(self.fileName,names=['input','out','weight'])
        edge_list = []
        for index, row in data_pd.iterrows():
            edge_list.append([row['input'],row['out'],row['weight']])
        graph_type.add_weighted_edges_from(edge_list)  # 添加边到图中
        graph_type=self.project_triangle(graph_type)
        graph_type=self.project_degree(graph_type)
        for i in graph_type.nodes():
            strength = 0
            for j in graph_type.nodes():
                weight = graph_type.get_edge_data(int(i), int(j))
                if weight is not None:
                    strength = strength + list(weight.values())[0]  # 得到每个节点的节点强度

            graph_type.add_node(i, degree_strength_triangleCount=[graph_type.degree(i), strength,nx.triangles(graph_type,i)])  # 将[节点度，节点强度]作为属性添加到每个节点上
            graph_type.add_node(i, triangle_count=nx.triangles(graph_type,i))
            # print(""+str(int(i))+"的度="+str(graph_type.degree(i))+"，强度="+str(strength)+"，三角计数="+str(int(count_n/2)))
        # print("[节点度，节点强度,三角计数]已完成")
        return graph_type



    # 获得[节点度，节点强度]加噪频率，敏感度2θ+1，隐私预算epsilon
    def getNodeFrequency(self):
        ds_frequency = []
        new_ds_frequency = []
        for i in self.degree_strength_triangleCount:
            sum_frequency = 0
            for j in self.degree_strength_triangleCount:
                if i == j:
                    sum_frequency = sum_frequency + 1
            ds_frequency.append([i, sum_frequency])
        for i in ds_frequency:
            if i not in new_ds_frequency:
                # 归一化
                new_ds_frequency.append(i)
        new_ds_frequency_count=[i[1] for i in new_ds_frequency]
        Sensitivity=max(2*self.degreeThreshold+1,4*self.triangleCountThreshold+1)
        new_ds_frequency_addnoise=laplace_mech(new_ds_frequency_count,Sensitivity,self.epsilon*0.4)#加噪
        for i in range(0,len(new_ds_frequency)):
            new_ds_frequency[i][1]=new_ds_frequency_addnoise[i]
        new_ds_frequency_sum=sum([x[1] for x in np.array(new_ds_frequency, dtype=list)])
        for i in new_ds_frequency:
            i[1] = i[1] / new_ds_frequency_sum
        new_ds_frequency.sort(key=lambda x:x[1])
        return new_ds_frequency

    #获得图的加噪权值分布，敏感度θ，隐私预算epsilon
    def getWeightFrequency(self):
        weight_list = []
        weight_frequency = []
        new_weight_frequency = []
        for i in self.projectGraph.edges():
            weight = self.projectGraph.get_edge_data(i[0], i[1])
            weight_list.append(list(weight.values())[0])
        for i in weight_list:
            count = 0
            for j in weight_list:
                if i == j:
                    count = count + 1
            weight_frequency.append([i, count])
        for i in weight_frequency:
            if i not in new_weight_frequency:
                new_weight_frequency.append(i)
        weight_frequency_count=[i[1] for i in new_weight_frequency]
        weight_frequency_count_addnoise=laplace_mech(weight_frequency_count,self.degreeThreshold,self.epsilon*0.4)
        for i in range(0,len(new_weight_frequency)):
            new_weight_frequency[i][1]=weight_frequency_count_addnoise[i]
        new_weight_frequency_sum=sum([x[1] for x in np.array(new_weight_frequency, dtype=list)])
        for i in new_weight_frequency:
            i[1] = i[1] / new_weight_frequency_sum
        # print(new_weight_frequency)
        return new_weight_frequency
