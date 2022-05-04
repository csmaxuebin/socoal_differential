import random
import networkx as nx
from collections import Counter
import scipy.stats as stats
import numpy as np



def random_pick(some_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item

#判断两个列表内的元素有没有重复
def just(ls):
    new_list = []
    for i in ls:
        if i not in new_list:
            new_list.append(i)
            # 这样能确保新的列表里包含原列表里所有种类的元素，且元素互不重复
    if len(new_list) == len(ls):
        print('原列表里的元素互不重复！')
    else:
        print('原列表里有重复的元素！')

# 生成总和固定的整数序列。maxvalue: 序列总和，num：要生成的整数个数
def random_num_with_fix_total(num, totleValue, some_list, probabilities):
    while True:
        a = []
        for i in range(0, num):
            a.append(random_pick(some_list, probabilities))
        total = 0
        for ele in range(0, len(a)):
            total = total + a[ele]
        if total == totleValue:
            break
    return a

#保存在txt文件
def save_to_txt(data, filename):
    fw = open(filename, 'w')
    for line in data:
        for a in range(0,len(line)):
            fw.write(str(line[a]))
            if a!=2:
                fw.write(',')
        fw.write('\n')
    fw.close()
def random_choices_node(graph,number):
    nodes=[]
    for i in range(0,number):
        j=random.choice(list(graph.nodes()))
        nodes.append(j)
    return nodes


#得到两个节点之间相连会产生多少三角形
def i_j_triangle(graph,i,j):
    return len(list(set(graph[i])&set(graph[j])))

#得到节点强度分布
def strength_histogram(G):

    counts = Counter(d for n, d in G.degree(weight='weight'))
    return [counts.get(i, 0) for i in range(max(counts) + 1)]

def triangle_count_histogram(G):
    counts = Counter(d for n, d in G.nodes.data('triangle_count'))

    return [counts.get(i, 0) for i in range(max(counts) + 1)]

'''#对图进行投影将结果保存在CSV文件中。data_name:文件名，data_name_project投影后的文件名，
def project(data_pd,degreeThreshold):
    nodeNumber = max(data_pd['input'].max(), data_pd['out'].max())  # 获得节点个数
    nodeDegree = {}
    for i in range(1, nodeNumber + 1):  # 为每个节点的节点度设置为0
        nodeDegree[i] = 0
    data_pd=data_pd.sort_values(by="weight", ascending=True)
    for index, row in data_pd.iterrows():
        if ((nodeDegree[row['input']] < degreeThreshold) & (nodeDegree[row['out']] < degreeThreshold)):
            nodeDegree[row['input']] += 1
            nodeDegree[row['out']] += 1
        else:  # 直接删除这条边
            data_pd.drop(index, inplace=True)
    return data_pd'''

#求某个节点的三角计数
def node_triangle_count(i,graph):
    return nx.triangles(graph,i)

# #找到与某个节点相连的最大度的节点
# def find_max_degree_node(i,graph):

#找到与某个节点相连的不形成三角形的度最大的节点,若没有则找到与节点相连的度最大的节点
#同于投影
def find_min_triangle_node(i,graph):
    max=0
    j=0
    for n_adj in graph[i]:
        count_i=0
        for x in graph[i]:
            if x in graph[n_adj]:
                count_i=count_i+1
        if count_i==0 and graph.degree(n_adj)>max:
            max=graph.degree(n_adj)
            j=n_adj
    if j==0:
        for n_adj in graph[i]:
            if graph.degree(n_adj)>max:
                max=graph.degree(n_adj)
                j=n_adj
    return j

#用于投影的时候根据三角阈值删除边
def find_max_triangle_node(i,graph):
    max=0
    j=None
    for n_adj in graph[i]:
        count_i=0
        for x in graph[i]:
            if x in graph[n_adj]:
                count_i=count_i+1
        if count_i>=max and j==None:
            max=count_i
            j=n_adj
        elif count_i>=max and graph.degree(n_adj)>graph.degree(j):
            max=count_i
            j=n_adj
    return j


'''
j是i三角数不满足的邻居节点
x是j三角形数不满足的邻居节点
'''
#
def find_neighbour_neighbour_1(i,graph):
    for j in graph[i]:
        triangle_j=nx.get_node_attributes(graph, 'degree_strength_triangleCount')[j][2]
        if node_triangle_count(j,graph)<triangle_j:
            for x in graph[j]:
                triangle_x=nx.get_node_attributes(graph, 'degree_strength_triangleCount')[x][2]
                if node_triangle_count(x,graph)<triangle_x \
                        and (i,x) not in graph.edges()\
                        and i!=x:
                    return x
    return None
def find_neighbour_neighbour_1_test(i,graph):
    triangle_i=nx.get_node_attributes(graph, 'degree_strength_triangleCount')[i][2]
    max=0
    index=None
    for j in graph.nodes():
        if j not in graph[i] and j!=i:
            product_triangle=i_j_triangle(graph,i,j)
            if max<product_triangle and product_triangle<=triangle_i-node_triangle_count(i,graph):
                max=product_triangle
                index=j
    # print("product="+str(max))
    return index
'''
j是与i不产生三角形的邻居节点中度最大的节点
'''
def find_neighbour_neighbour_3(i,graph):
    max=0
    index=None
    for j in graph[i]:
        if i_j_triangle(graph,i,j)==0 and graph.degree(j)>max:
            max=graph.degree(j)
            index=j
    return index

'''
j是i的三角形过多的邻居节点
X是j的三角形过多的邻居节点，并且x也是i的邻居节点
'''
def find_neighbour_neighbour_2(i,graph):
    for j in graph[i]:
        triangle_j=nx.get_node_attributes(graph, 'degree_strength_triangleCount')[j][2]
        if node_triangle_count(j,graph)>triangle_j:
            for x in graph[j]:
                triangle_x=nx.get_node_attributes(graph, 'degree_strength_triangleCount')[x][2]
                if node_triangle_count(x,graph)>triangle_x \
                        and (i,x) in graph.edges() \
                        and i!=x:
                    return x
    return None
def find_neighbour_neighbour_2_test(i,graph):
    max =9999
    index=None
    for j in graph[i]:
        triangle_j=nx.get_node_attributes(graph, 'degree_strength_triangleCount')[j][2]
        if node_triangle_count(j,graph)>triangle_j:
            for x in graph[j]:
                triangle_x=nx.get_node_attributes(graph, 'degree_strength_triangleCount')[x][2]
                if node_triangle_count(x,graph)>triangle_x \
                        and (i,x) in graph.edges() \
                        and i!=x and i_j_triangle(graph,i,x)<max:
                    max=i_j_triangle(graph,i,x)
                    index=x
    return index

#x寻找与vi不相连的节点中，不会产生新的三角形，最好的情况是度也未满足
def find_notriangle(i,graph):
    count=0
    index=None
    for j in graph.nodes():
        if  (i,j) not in graph.edges()\
            and graph.degree(j)<graph.nodes[j]['degree_strength_triangleCount'][0]:
            for x in graph[i]:
                if x in graph[j]:
                    count=count+1
            if count==0:
                break
    return index
#x寻找与vi相连的节点中，不会产生新的三角形，最好的情况是度也未满足
# def find_join_notriangle(i,graph):


#求两个列表的KS距离
def KS_distance(list1,list2):
    while True:
        if len(list1)<len(list2):
            list1.append(0)
        elif len(list1)>len(list2):
            list2.append(0)
        else:
            break
    return stats.ks_2samp(list1,list2)
#求两个列表的L1距离
def L1_error(list1,list2):

    while True:
        if len(list1)<len(list2):
            list1.append(0)
        elif len(list1)>len(list2):
            list2.append(0)
        else:
            break
    # print(list1)
    # print(list2)
    return np.sum(np.abs(np.array(list1)-np.array(list2)))
#获得图的局部聚类系数的相对误差
def local_cluster_SE(originalWeightGraph,SyntheticWeightGraph):
    originalLocalCluser=nx.clustering(originalWeightGraph)
    originalMeanLocalCluser=sum(originalLocalCluser.values())/len(originalLocalCluser)

    SyntheticLocalCluser=nx.clustering(SyntheticWeightGraph)
    SyntheticMeanLocalCluser=sum(SyntheticLocalCluser.values())/len(SyntheticLocalCluser)
    # print(originalLocalCluser,originalMeanLocalCluser,SyntheticLocalCluser,SyntheticMeanLocalCluser)
    # print(originalMeanLocalCluser,SyntheticMeanLocalCluser)
    return abs(originalMeanLocalCluser-SyntheticMeanLocalCluser)/SyntheticMeanLocalCluser

#获得图的边数的相对误差
def edgeNumber_SE(originalWeightGraph,SyntheticWeightGraph):
    originalEdgeNumber=len(originalWeightGraph.edges())
    SyntheticEdgeNumber=len(SyntheticWeightGraph.edges())
    print("实际和现有，"+str(originalEdgeNumber)+"，"+str(SyntheticEdgeNumber))
    return abs(originalEdgeNumber-SyntheticEdgeNumber)/SyntheticEdgeNumber

def triangleNumber_SE(originalWeightGraph,SyntheticWeightGraph):
    originalTriangleNumber=sum(nx.triangles(originalWeightGraph).values())/3
    SyntheticTriangleNumber=sum(nx.triangles(SyntheticWeightGraph).values())/3
    print("实际和现有，"+str(originalTriangleNumber)+"，"+str(SyntheticTriangleNumber))
    # print(originalTriangleNumber,SyntheticTriangleNumber)
    return abs(originalTriangleNumber-SyntheticTriangleNumber)/SyntheticTriangleNumber
def in_1(a,b,c):
    print("节点"+str(a)+"的分配三角"+str(b)+"，实际三角"+str(c))