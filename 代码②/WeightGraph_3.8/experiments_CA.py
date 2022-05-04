import pickle
import time

from OriginalWeightGraph_2 import OriginalWeightGraph_2
from SyntheticWeightGraph_test import SyntheticWeightGraph
from tool_2 import *
import matplotlib.pyplot as plt
import scipy.stats as stats

if __name__ == '__main__':
    for j in range(0, 5):
        e = [0.1, 0.5, 1.0, 1.5, 2.0]
        for i in e:
                start_time = time.asctime(time.localtime(time.time()))
                print(start_time)
                f = open("object_noproj/CA_noproj_"+str(i), "rb")
                original = pickle.load(f)
                f.close()
                print("隐私预算" + str(original.epsilon))
                print(original.triangleCountThreshold)
                print(original.degreeThreshold)
                syn = SyntheticWeightGraph(original)
                print("SyntheticWeightGraph")
                original_1=pickle.dumps(syn)
                with open("syn-nproj/syn_CA_addnoise_"+str(i)+"_"+str(j), "ab")as f:
                        f.write(original_1)
                f.close()

                print("over")
                print("degree-KS=" + str(KS_distance(nx.degree_histogram(original.originalGraph), nx.degree_histogram(syn.G))))
                print("degree-1=" + str(L1_error(nx.degree_histogram(original.originalGraph), nx.degree_histogram(syn.G))))
                print("Strength-KS=" + str(KS_distance(strength_histogram(original.originalGraph), strength_histogram(syn.G))))
                print("Strength-L1=" + str(L1_error(strength_histogram(original.originalGraph), strength_histogram(syn.G))))

                print("triangle-KS=" + str(
                    KS_distance(triangle_count_histogram(original.originalGraph), triangle_count_histogram(syn.G))))
                print("triangle-L1=" + str(
                    L1_error(triangle_count_histogram(original.originalGraph), triangle_count_histogram(syn.G))))
                print("局部聚类" + str(local_cluster_SE(original.originalGraph, syn.G)))
                print("N-edge=" + str(edgeNumber_SE(original.originalGraph, syn.G)))
                print("N-triangele=" + str(triangleNumber_SE(original.originalGraph, syn.G)))

                last_time = time.asctime(time.localtime(time.time()))
                print(last_time)
