 #!/usr/bin/python3
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib 

series = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series') #首先创建一个Series对象 

series.plot.pie(figsize=(6, 6))#绘制饼图，图片规格为figsize=(6, 6) 
df = pd.DataFrame(3 * np.random.rand(4, 2), index=['a', 'b', 'c', 'd'], columns=['x', 'y']) 
df.plot.pie(subplots=True, figsize=(8, 4)) 

#series.plot.pie(labels=['AA', 'BB', 'CC', 'DD'], colors=['r', 'g', 'b', 'c'], autopct='%.2f', fontsize=20, figsize=(6, 6)) 
plt.show()