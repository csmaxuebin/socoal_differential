import pickle



import time

from OriginalWeightGraph_2 import OriginalWeightGraph_2
from SyntheticWeightGraph_test import SyntheticWeightGraph
from tool import *
import matplotlib.pyplot as plt
import scipy.stats as stats

if __name__ == '__main__':
            start_time = time.asctime(time.localtime(time.time()))
            print(start_time)
            f=open("object/soc-sign-bitcoinotc-Pretreatment_1.0","rb")
            original = pickle.load(f)
            print("隐私预算"+str(original.epsilon))
            print(original.triangleCountThreshold)
            print(original.degreeThreshold)
            syn = SyntheticWeightGraph(original)
            syn_1=pickle.dumps(syn)
            print("SyntheticWeightGraph")

            print("degree-KS="+str(KS_distance(nx.degree_histogram(original.originalGraph),nx.degree_histogram(syn.G))))
            print("degree-1="+str(L1_error(nx.degree_histogram(original.originalGraph),nx.degree_histogram(syn.G))))


            print("Strength-KS="+str(KS_distance(strength_histogram(original.originalGraph),strength_histogram(syn.G))))
            print("Strength-L1="+str(L1_error(strength_histogram(original.originalGraph),strength_histogram(syn.G))))

            print("triangle-KS="+str(KS_distance(triangle_count_histogram(original.originalGraph),triangle_count_histogram(syn.G))))
            print("triangle-L1="+str(L1_error(triangle_count_histogram(original.originalGraph),triangle_count_histogram(syn.G))))
            print("局部聚类"+str(local_cluster_SE(original.originalGraph,syn.G)))
            print("N-edge="+str(edgeNumber_SE(original.originalGraph,syn.G)))
            print("N-triangele="+str(triangleNumber_SE(original.originalGraph,syn.G)))

            with open("syn_bto_1.0","ab")as f:
                f.write(syn_1)
            print("over")
            last_time = time.asctime(time.localtime(time.time()))
            print(last_time)

