#!/usr/bin/python3
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib 

series=Series(np.array([2.5, 4.1, 2.7, 8.8, 1.0]))
series.plot(linestyle='dashed', color='k', marker='o') 
series.index.name='site'
plt.show()
