
from ComparisonMethod import OriginalWeightGraph_2
import networkx as nx
import pickle
from Laplace import laplace_mech
e=[0.1,0.5,1.0,1.5,2.0]
for i in e:
    f = open("comparison/Comparison_CA_"+str(i), "rb")
    original = pickle.load(f)
    f.close()
    edgeNumberlist=[len(original.originalGraph.edges())]
    edgeNumber=edgeNumberlist[0]
    edgeNumberNoiselist=laplace_mech(edgeNumberlist,original.degreeThreshold+100,i/2)
    edgeNumberNoise=edgeNumberNoiselist[0]
    # print(edgeNumber,edgeNumberNoise)
    print(abs(edgeNumber-edgeNumberNoise)/edgeNumber)