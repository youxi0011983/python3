 #!/usr/bin/python3
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib 


dataframe=DataFrame({'A':[9.3, 4.3, 4.1, 5.0, 7.0], 'B':[2.5, 4.1, 2.7, 8.8, 1.0]})
dataframe.plot(kind='bar')                                                                                                      #垂直柱状图
dataframe.index=['once', 'twice', 'thrice', 'forth', 'fifth'] 
plt.show()


dataframe.plot(kind='barh')                                                                                                     #水平柱状图
plt.show()

