#!/usr/bin/python3
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib 

df4 = DataFrame({'a': np.random.randn(1000) + 1, 
    'b': np.random.randn(1000),
    'c': np.random.randn(1000) - 1}, 
    index=range(1,1001), columns=['a', 'b', 'c']) 


plt.figure()

df4.plot.hist(stacked=True, bins=500, alpha=0.5)        #bins=20表示数值分辨率，具体来说是将随机数设定一个范围，例如5.6，5.7，6.5，如果数值分辨率越低，则会将三个数分到5-7之间，如果数值分辨率越高，则会将5.6，5.7分到5-6之间，而6.5分到6-7之间；值越小表示分辨率越低，值越大表示分辨率越高；



#df4['a'].plot.hist(orientation='horizontal', cumulative=True)  #该图是将DataFrame对象当中的a进行数值累加，并绘制横向直方图，横轴表示频率（Frequency），纵轴表示数值，cumulative=True的效果是将Frequency的数值从大到小进行排列。
#df4.diff().hist(color='k', alpha=0.5, bins=50) #该效果是将DataFrame当中column分开，即将a，b和c分开绘制成三张图。df4.diff().hist()可达到这个效果，即将所有column分开。
plt.show()