 #!/usr/bin/python3
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib 

dataframe=DataFrame({'A':[9.3, 4.3, 4.1, 5.0, 7.0], 'B':[2.5, 4.1, 2.7, 8.8, 1.0]}) 

dataframe.plot(linestyle='dashed', color='k', marker='o', xticks=[0, 1, 2, 3, 4], yticks=list(np.arange(0, 10.0, 0.5)) ,xlim=[-0.25, 4.25]) 
dataframe.plot(title='dataframe photo')
dataframe.plot(subplots=True, sharex=True)
plt.show()