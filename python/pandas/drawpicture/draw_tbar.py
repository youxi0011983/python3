 #!/usr/bin/python3
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib 


df=DataFrame({'part A': [2.8, 5.5, 4.5, 7.0, 1.0], 
    'part B': [4.2, 1.2, 4.5, 2.5, 8.0], 
    'part C': [3.0, 3.3, 1.0, 0.5, 1.0]}, 
    index=['May', 'June', 'July', 'August', 'September']) 

df.name='bonus'
df.plot(kind='barh',stacked=True)
df.plot.barh(stacked=True)
plt.show()