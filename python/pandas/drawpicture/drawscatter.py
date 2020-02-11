 #!/usr/bin/python3
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib 

df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])  #abcd四列中，各列设定50个随机数 
#df.plot.scatter(x='a',y='b')    #之后以a列为X轴数值，b列为Y轴数值绘制散点图 

#ax = df.plot.scatter(x='a', y='b', color='DarkBlue', label='Group 1') #先设定第一个散点图，颜色为深蓝色标签为
#df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=ax) #第二个散点图以cd两列作为x及y轴的值，

ab=df.plot.scatter(x='a', y='b', color='DarkBlue', label='Group 1') #a列与b列的绘图关系 
abcd=df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=ab) #将ab的绘图关系嵌套到c列和d列的绘图关系中：ax=ab 
abcdac=df.plot.scatter(x='a', y='c', color='DarkRed', label='Group 3', ax=abcd) #将ab的绘图关系及cd的绘图关系的汇总关系当中加入到a列和c列的绘图关系中：ax=abcd 
df.plot.scatter(x='b', y='d', color='DarkGray', label='Group 4', ax=abcdac) #将上述3种关系的绘图嵌套到b列和d列的绘图关系中：ax=abcdac

#df.plot.scatter(x='a', y='b', c='c', s=50) #c参数设定为df的第c列数值，表示的是绘制的点的灰度水平，同时灰度水平会出现一个灰度梯度标签表示不同的灰度级别。
df.plot.scatter(x='a', y='b', s=df['c']*200)#用df的c列数值的200倍表示点的大小


plt.show()