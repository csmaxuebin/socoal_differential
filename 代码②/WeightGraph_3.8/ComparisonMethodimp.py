from ComparisonMethod import OriginalWeightGraph_2
import pickle
e=[0.1,0.5,1.0,1.5,2.0]
for i in e:
    original = OriginalWeightGraph_2("data/soc-sign-bitcoinotc-Pretreatment.csv", i)
    original_1=pickle.dumps(original)
    with open("comparison/Comparison_method_BTO_"+str(i), "ab")as f:
        f.write(original_1)
    f.close()

    original = OriginalWeightGraph_2("data/CA-GrQC.csv", i)
    original_1=pickle.dumps(original)
    with open("comparison/Comparison_method_CA_GrQC_"+str(i), "ab")as f:
        f.write(original_1)
    f.close()

    original = OriginalWeightGraph_2("data/lastfm_asia_edges.csv", i)
    original_1=pickle.dumps(original)
    with open("comparison/Comparison_method_lastfm_asia_edges_"+str(i), "ab")as f:
        f.write(original_1)
    f.close()

