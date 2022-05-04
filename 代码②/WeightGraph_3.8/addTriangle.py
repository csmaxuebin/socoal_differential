from ComparisonMethod import OriginalWeightGraph_2
import networkx as nx
import pickle
from Laplace import laplace_mech

e=[0.1,0.5,1.0,1.5,2.0]
for i in e:
    f = open("Comparison_lastfm_asia_edges_"+str(i), "rb")
    original = pickle.load(f)
    f.close()
    for n in original.NoiseGraph.nodes():#遍历所有节点
        original.NoiseGraph.add_node(n, triangle_count=nx.triangles(original.NoiseGraph,n))
    original_1=pickle.dumps(original)
    with open("Comparison_lastfm_asia_"+str(i), "ab")as f:
        f.write(original_1)
    f.close()