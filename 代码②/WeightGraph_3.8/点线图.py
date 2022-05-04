import matplotlib.pyplot as plt
import numpy as np
import math

import csv
with open('投影对比数据.CSV', 'r',encoding='utf-8')as f:
    cs = list(csv.reader(f))


plt.figure(figsize=(20, 12))
x_data = ['0.1','0.5','1.0','1.5','2.0']
ax1 = plt.subplot(2,4,1)#指定ax1占用第一行(0)整行

plt.title('degree-KS')
ax2 = plt.subplot(2,4,2)#指定ax2占用第二行(1)的第一格(第二个参数为0)
plt.title('strength-KS')
ax3 = plt.subplot(2,4,3)
plt.title('triangle-KS')
ax4 = plt.subplot(2,4,4)
plt.title('edge-MRE')

ax5 = plt.subplot(2,4,5)
plt.title('degree-L1')

ax6 = plt.subplot(2,4,6)
plt.title('strength-L1')

ax7 = plt.subplot(2,4,7)
plt.title('triangle-L1')
ax8 = plt.subplot(2,4,8)
plt.title('triangle-MRE')
#KS-度
data0=[float(x) for x in cs[0]]
data1=[float(x) for x in cs[1]]
data2=[float(x) for x in cs[2]]
data3=[float(x) for x in cs[3]]
data4=[float(x) for x in cs[4]]
data5=[float(x) for x in cs[5]]

line1=ax1.plot(x_data,data0,color='red',linewidth=2.0,linestyle='--',marker='o',label='Bitcoin OTC-NAS')
line2=ax1.plot(x_data,data1,color='red',linewidth=2.0,marker='>',label='Bitcoin OTC-Noproj-NAS')
line3=ax1.plot(x_data,data2,color='blue',linewidth=2.0,linestyle='--',marker='o',label='Arxiv GR QC-NAS')
line4=ax1.plot(x_data,data3,color='blue',linewidth=2.0,marker='>',label='Arxiv GR QC-Noproj-NAS')
line5=ax1.plot(x_data,data4,color='green',linewidth=2.0,linestyle='--',marker='o',label='LastFM-NAS')
line6=ax1.plot(x_data,data5,color='green',linewidth=2.0,marker='>',label='LastFM-Noproj-NAS')
ax1.legend(loc=3, ncol=6,bbox_to_anchor=(-0.4,1.15),borderaxespad = 0.)
# plt.legend([line1,line2,line3,line4,line5,line6],["1","2","3","4","5","6"],loc='lower right', scatterpoints=1)
#L1-度
data6=[float(x) for x in cs[6]]
data7=[float(x) for x in cs[7]]
data8=[float(x) for x in cs[8]]
data9=[float(x) for x in cs[9]]
data10=[float(x) for x in cs[10]]
data11=[float(x) for x in cs[11]]

line1=ax5.plot(x_data,data6,color='red',linewidth=2.0,linestyle='--',marker='o')
line2=ax5.plot(x_data,data7,color='red',linewidth=2.0,marker='>')
line3=ax5.plot(x_data,data8,color='blue',linewidth=2.0,linestyle='--',marker='o')
line4=ax5.plot(x_data,data9,color='blue',linewidth=2.0,marker='>')
line5=ax5.plot(x_data,data10,color='green',linewidth=2.0,linestyle='--',marker='o')
line6=ax5.plot(x_data,data11,color='green',linewidth=2.0,marker='>')

#KS-强度
data12=[float(x) for x in cs[12]]
data13=[float(x) for x in cs[13]]
data14=[float(x) for x in cs[14]]
data15=[float(x) for x in cs[15]]
data16=[float(x) for x in cs[16]]
data17=[float(x) for x in cs[17]]

line1=ax2.plot(x_data,data12,color='red',linewidth=2.0,linestyle='--',marker='o')
line2=ax2.plot(x_data,data13,color='red',linewidth=2.0,marker='>')
line3=ax2.plot(x_data,data14,color='blue',linewidth=2.0,linestyle='--',marker='o')
line4=ax2.plot(x_data,data15,color='blue',linewidth=2.0,marker='>')
line5=ax2.plot(x_data,data16,color='green',linewidth=2.0,linestyle='--',marker='o')
line6=ax2.plot(x_data,data17,color='green',linewidth=2.0,marker='>')
#L1-强度
data18=[float(x) for x in cs[18]]
data19=[float(x) for x in cs[19]]
data20=[float(x) for x in cs[20]]
data21=[float(x) for x in cs[21]]
data22=[float(x) for x in cs[22]]
data23=[float(x) for x in cs[23]]

line1=ax6.plot(x_data,data18,color='red',linewidth=2.0,linestyle='--',marker='o')
line2=ax6.plot(x_data,data19,color='red',linewidth=2.0,marker='>')
line3=ax6.plot(x_data,data20,color='blue',linewidth=2.0,linestyle='--',marker='o')
line4=ax6.plot(x_data,data21,color='blue',linewidth=2.0,marker='>')
line5=ax6.plot(x_data,data22,color='green',linewidth=2.0,linestyle='--',marker='o')
line6=ax6.plot(x_data,data23,color='green',linewidth=2.0,marker='>')
#KS-三角
data24=[float(x) for x in cs[24]]
data25=[float(x) for x in cs[25]]
data26=[float(x) for x in cs[26]]
data27=[float(x) for x in cs[27]]
data28=[float(x) for x in cs[28]]
data29=[float(x) for x in cs[29]]

line1=ax3.plot(x_data,data24,color='red',linewidth=2.0,linestyle='--',marker='o')
line2=ax3.plot(x_data,data25,color='red',linewidth=2.0,marker='>')
line3=ax3.plot(x_data,data26,color='blue',linewidth=2.0,linestyle='--',marker='o')
line4=ax3.plot(x_data,data27,color='blue',linewidth=2.0,marker='>')
line5=ax3.plot(x_data,data28,color='green',linewidth=2.0,linestyle='--',marker='o')
line6=ax3.plot(x_data,data29,color='green',linewidth=2.0,marker='>')
#L1-三角
data30=[float(x) for x in cs[30]]
data31=[float(x) for x in cs[31]]
data32=[float(x) for x in cs[32]]
data33=[float(x) for x in cs[33]]
data34=[float(x) for x in cs[34]]
data35=[float(x) for x in cs[35]]

line1=ax7.plot(x_data,data30,color='red',linewidth=2.0,linestyle='--',marker='o')
line2=ax7.plot(x_data,data31,color='red',linewidth=2.0,marker='>')
line3=ax7.plot(x_data,data32,color='blue',linewidth=2.0,linestyle='--',marker='o')
line4=ax7.plot(x_data,data33,color='blue',linewidth=2.0,marker='>')
line5=ax7.plot(x_data,data34,color='green',linewidth=2.0,linestyle='--',marker='o')
line6=ax7.plot(x_data,data35,color='green',linewidth=2.0,marker='>')


data36=[float(x) for x in cs[36]]
data37=[float(x) for x in cs[37]]
data38=[float(x) for x in cs[38]]
data39=[float(x) for x in cs[39]]
data40=[float(x) for x in cs[40]]
data41=[float(x) for x in cs[41]]

line1=ax4.plot(x_data,data36,color='red',linewidth=2.0,linestyle='--',marker='o')
line2=ax4.plot(x_data,data37,color='red',linewidth=2.0,marker='>')
line3=ax4.plot(x_data,data38,color='blue',linewidth=2.0,linestyle='--',marker='o')
line4=ax4.plot(x_data,data39,color='blue',linewidth=2.0,marker='>')
line5=ax4.plot(x_data,data40,color='green',linewidth=2.0,linestyle='--',marker='o')
line6=ax4.plot(x_data,data41,color='green',linewidth=2.0,marker='>')
#L1-三角
data42=[float(x) for x in cs[42]]
data43=[float(x) for x in cs[43]]
data44=[float(x) for x in cs[44]]
data45=[float(x) for x in cs[45]]
data46=[float(x) for x in cs[46]]
data47=[float(x) for x in cs[47]]

line1=ax8.plot(x_data,data42,color='red',linewidth=2.0,linestyle='--',marker='o')
line2=ax8.plot(x_data,data43,color='red',linewidth=2.0,marker='>')
line3=ax8.plot(x_data,data44,color='blue',linewidth=2.0,linestyle='--',marker='o')
line4=ax8.plot(x_data,data45,color='blue',linewidth=2.0,marker='>')
line5=ax8.plot(x_data,data46,color='green',linewidth=2.0,linestyle='--',marker='o')
line6=ax8.plot(x_data,data47,color='green',linewidth=2.0,marker='>')



plt.show()