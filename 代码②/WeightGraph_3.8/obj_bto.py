import pickle
from OriginalWeightGraph_2 import OriginalWeightGraph_2
original = OriginalWeightGraph_2("data/soc-sign-bitcoinotc-Pretreatment.csv",2)
original_1=pickle.dumps(original)
with open("object/soc-sign-bitcoinotc-Pretreatment_2.0", "ab")as f:
    f.write(original_1)

#读取文件中的对象文件
#pickle.load()一次只读取一个对象文件
f=open("object/soc-sign-bitcoinotc-Pretreatment_2.0", "rb")
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
