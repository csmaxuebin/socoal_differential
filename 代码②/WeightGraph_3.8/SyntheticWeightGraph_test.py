
from tool_2 import *


class SyntheticWeightGraph:
    def __init__(self, originalWeightGraph):
        self.originalWeightGraph = originalWeightGraph
        self.G = self.getGraph()
        self.degree_and_strength = list(nx.get_node_attributes(self.G, 'degree_strength_triangleCount').values())
        self.post_deleteEdge()

    # 得到和原始图一样的节点集合
    def getGraph(self):
        ds_frequency = self.originalWeightGraph.ds_frequency
        # print(ds_frequency)
        ds_frequency_list = [x[0] for x in np.array(ds_frequency, dtype=list)]
        ds_frequency_probabilities = [x[1] for x in np.array(ds_frequency, dtype=list)]

        graph_type = nx.Graph()
        for i in self.originalWeightGraph.projectGraph.nodes():
            graph_type.add_node(i, degree_strength_triangleCount=random_pick(ds_frequency_list,
                                                                                 ds_frequency_probabilities))
        originalEdgeNumber = self.originalWeightGraph.edge_number
        degreeCount = 0
        triangleCount=0
        for i in graph_type.nodes():
            degreeCount = degreeCount + graph_type.nodes[i]['degree_strength_triangleCount'][0]
            triangleCount=triangleCount+graph_type.nodes[i]['degree_strength_triangleCount'][2]
        degreeCount = degreeCount / 2
        triangleCount=triangleCount/3
        print("分配的"+str(degreeCount)+",加噪总边"+str(originalEdgeNumber))
        print("分配的三角"+str(triangleCount)+",加噪总三角"+str(self.originalWeightGraph.triangleNumber))
        weight_frequency_list = [x[0] for x in np.array(self.originalWeightGraph.weight_frequency, dtype=list)]
        weight_frequency_probabilities = [x[1] for x in np.array(self.originalWeightGraph.weight_frequency, dtype=list)]
        noiseEdge=self.originalWeightGraph.edge_number
        noiseTriangleNumber=self.originalWeightGraph.triangleNumber
        print("str(noiseEdge)"+str(noiseEdge))
        print("str(noiseTriangleNumber)"+str(noiseTriangleNumber))

        while len(graph_type.edges())<noiseEdge:
            node =random_choices_node(graph_type, 2)
            i=node[0]
            j=node[1]
            degree_i = nx.get_node_attributes(graph_type, 'degree_strength_triangleCount')[i][0]
            degree_j = nx.get_node_attributes(graph_type, 'degree_strength_triangleCount')[j][0]
            strength_i = nx.get_node_attributes(graph_type, 'degree_strength_triangleCount')[i][1]
            strength_j = nx.get_node_attributes(graph_type, 'degree_strength_triangleCount')[j][1]
            weight = random_pick(weight_frequency_list, weight_frequency_probabilities)
            if (i,j) not in graph_type.edges() \
                    and degree_j > graph_type.degree(j) \
                    and degree_i > graph_type.degree(i) \
                    and weight < (strength_i - graph_type.degree(i, weight='weight')) \
                    and weight < (strength_j - graph_type.degree(j, weight='weight')):
                weight = random_pick(weight_frequency_list, weight_frequency_probabilities)
                graph_type.add_edge(i, j, weight=weight)
                # print("添加（"+str(i)+","+str(j)+")初始~~~~~~~~~~~~")
        return graph_type
    def test(self):
        originalEdgeNumber = len(self.originalWeightGraph.originalGraph.edges())
        originalTriangleNumber = sum(nx.triangles(self.originalWeightGraph.originalGraph).values()) / 3
        degreeCount = 0
        triangleCount = 0
        for i in self.G.nodes():
            triangleCount = triangleCount + self.G.nodes[i]['degree_strength_triangleCount'][2]
            degreeCount = degreeCount + self.G.nodes[i]['degree_strength_triangleCount'][0]
        degreeCount = degreeCount / 2
        triangleCount = triangleCount / 3
        # print(originalEdgeNumber, degreeCount)
        print("str(abs(originalEdgeNumber - degreeCount) / degreeCount))-edge=" + str(abs(originalEdgeNumber - degreeCount) / degreeCount))
        print(originalTriangleNumber, triangleCount)
        print("△str(abs(originalTriangleNumber - triangleCount) / triangleCount))-edge=" + str(abs(originalTriangleNumber - triangleCount) / triangleCount))

    def post_deleteEdge(self):
        weight_frequency_list = [x[0] for x in np.array(self.originalWeightGraph.weight_frequency, dtype=list)]
        weight_frequency_probabilities = [x[1] for x in np.array(self.originalWeightGraph.weight_frequency, dtype=list)]
        print(self.G.nodes())
        for i in self.G.nodes():
            if self.originalWeightGraph.triangleNumber<sum(nx.triangles(self.G).values())/3:
                break
            # print("节点"+str(i))
            triangle_i = nx.get_node_attributes(self.G, 'degree_strength_triangleCount')[i][2]
            while node_triangle_count(i,self.G)<triangle_i:
                neighbour_neighbour_1=find_neighbour_neighbour_1_test(i,self.G)
                if neighbour_neighbour_1!=None:
                    weight = random_pick(weight_frequency_list, weight_frequency_probabilities)
                    self.G.add_edge(i, neighbour_neighbour_1, weight=weight)
                    # print("add（"+str(i)+","+str(neighbour_neighbour_1)+")one~~~~~~~~~~~~")
                else:break
        for i in self.G.nodes():
            # print("node"+str(i))
            while  node_triangle_count(i,self.G)>triangle_i:
                neighbour_neighbour_2=find_neighbour_neighbour_2_test(i,self.G)
                if neighbour_neighbour_2!=None:
                    self.G.remove_edge(i,neighbour_neighbour_2)
                    # print("delete（"+str(i)+","+str(neighbour_neighbour_2)+")Two")
                else:break
        for i in self.G.nodes():
            count_n = 0
            for n_adj in self.G[i]:  # 访问节点的邻接节点
                for x in self.G[i]:
                    if x in self.G[n_adj]:
                        count_n = count_n + 1  # 寻找有多少个共同节点
            self.G.add_node(i, triangle_count=int(count_n / 2))

