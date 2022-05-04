import pickle
import time
from ComparisonMethod import OriginalWeightGraph_2
from tool_2 import *


if __name__ == '__main__':

    a = [0.1, 0.5, 1.0, 1.5, 2.0]
    for e in a:

        print("-----------隐私预算="+str(e)+"---------------")
        f1=open("CA-GrQC_addnoise_"+str(e)+"_0", "rb")
        comparison_method_BTO = pickle.load(f1)
        f2=open("../object/CA-GrQC_"+str(e), "rb")
        original = pickle.load(f2)

        print("degree-KS="+str(KS_distance(nx.degree_histogram(original.originalGraph),nx.degree_histogram(comparison_method_BTO.G))))
        print("degree-1="+str(L1_error(nx.degree_histogram(original.originalGraph),nx.degree_histogram(comparison_method_BTO.G))))


        print("Strength-KS="+str(KS_distance(strength_histogram(original.originalGraph),strength_histogram(comparison_method_BTO.G))))
        print("Strength-L1="+str(L1_error(strength_histogram(original.originalGraph),strength_histogram(comparison_method_BTO.G))))

        print("triangle-KS="+str(KS_distance(triangle_count_histogram(original.originalGraph),triangle_count_histogram(comparison_method_BTO.G))))
        print("triangle-L1="+str(L1_error(triangle_count_histogram(original.originalGraph),triangle_count_histogram(comparison_method_BTO.G))))

        print("N-edge="+str(edgeNumber_SE(original.originalGraph,comparison_method_BTO.G)))
        print("N-triangele="+str(triangleNumber_SE(original.originalGraph,comparison_method_BTO.G)))

        f1.close()
        f2.close()
        last_time = time.asctime(time.localtime(time.time()))
        print(last_time)

