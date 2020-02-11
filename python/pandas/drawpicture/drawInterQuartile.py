 #!/usr/bin/python3
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib 

df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E']) 
color = dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')

#df.plot.box(color=color, sym='r+')
df.plot.box(vert=False, positions=[1, 4, 5, 6, 8])
plt.show()