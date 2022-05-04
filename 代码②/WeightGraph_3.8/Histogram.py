# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)

# cpmparison_data=[5720,5682,5676,5660,5598]
# syn_data=[3202,3164,3136,3122,3042]
cpmparison_data=[0.175675676,0.172297297,0.168918919,0.165540541,0.165540541]
syn_data=[0.065315315,0.054054054,0.054054054,0.050675676,0.047297297]

x=[0.1,0.5,1.0,1.5,2.0]
width=0.15
plt.bar(x[0]-width/2, cpmparison_data[0], width,label='DP', color="w",edgecolor="k",hatch="..")
plt.bar(x[0]+width/2, syn_data[0],width,label='Our algorithm',color="w",edgecolor="k",hatch="||")
plt.bar(x[1]-width/2, cpmparison_data[1], width, color="w",edgecolor="k",hatch="..")
plt.bar(x[1]+width/2, syn_data[1], width, color="w",edgecolor="k",hatch="||")
plt.bar(x[2]-width/2, cpmparison_data[2], width, color="w",edgecolor="k",hatch="..")
plt.bar(x[2]+width/2, syn_data[2], width, color="w",edgecolor="k",hatch="||")
plt.bar(x[3]-width/2, cpmparison_data[3], width, color="w",edgecolor="k",hatch="..")
plt.bar(x[3]+width/2, syn_data[3], width, color="w",edgecolor="k",hatch="||")
plt.bar(x[4]-width/2, cpmparison_data[4], width, color="w",edgecolor="k",hatch="..")
plt.bar(x[4]+width/2, syn_data[4], width, color="w",edgecolor="k",hatch="||")


# x: 条形图x轴
# y：条形图的高度
# width：条形图的宽度 默认是0.8
# bottom：条形底部的y坐标值 默认是0
# align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘

plt.legend()
plt.xticks(x)
plt.xlabel('epsilon')
plt.ylabel('value')

plt.title(u'测试例子——条形图', FontProperties=font)

plt.show()
