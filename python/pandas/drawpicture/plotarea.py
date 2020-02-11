#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib 


df = pd.DataFrame({
    'sales': [3, 2, 3, 9, 10, 6,3, 2, 3, 9, 10, 6],
    'signups': [5, 5, 6, 12, 14, 13,5, 5, 6, 12, 14, 13],
    'visits': [20, 42, 28, 62, 81, 50,20, 42, 28, 62, 81, 50],
}, index=pd.date_range(start='2018/01/01', periods=12,freq='M'))
#print(df)

ax = df.plot.area()
plt.show()