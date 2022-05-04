import pickle
from OriginalWeightGraph_noproj import OriginalWeightGraph_2
e=[0.1,0.5,1.0,1.5,2.0]
for i in e:
    original = OriginalWeightGraph_2("data/lastfm_asia_edges.csv",i)
    original_1=pickle.dumps(original)
    with open("object_noproj/lastfm_asia_noproj_"+str(i), "ab")as f:
        f.write(original_1)
    f.close()
    #读取文件中的对象文件
    #pickle.load()一次只读取一个对象文件
    f=open("object_noproj/lastfm_asia_noproj_"+str(i), "rb")
    while 1:
        try:
            obj = pickle.load(f)
            print(obj.epsilon,obj)
            print(obj.triangleCountThreshold,obj)
            A=obj.degree_strength_triangleCount
            print(A)
        except:
            break
    f.close()
