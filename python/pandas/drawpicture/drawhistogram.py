#!/usr/bin/python3
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib 

length=DataFrame({'length': [10, 20,15,10,1,12,12,12,13,13,13,14,14,14,51,51,51,51,51,4,4,4,4]})
length.plot.hist()
length.plot.density(color='k')
plt.show()
