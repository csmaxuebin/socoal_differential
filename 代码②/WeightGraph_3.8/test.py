import pickle


my_list = [123,3.14,'春秋大梦',[123,'rrr']]

original_1=pickle.dumps(my_list)
e=0.4
with open("lmy_list"+str(e),"ab")as f:
    f.write(original_1)
f.close()
#读取文件中的对象文件
#pickle.load()一次只读取一个对象文件

f=open("object/soc-sign-bitcoinotc-Pretreatment_0.1","rb")
original = pickle.load(f)
print(original.degreeThreshold,original.triangleCountThreshold)
f.close()
