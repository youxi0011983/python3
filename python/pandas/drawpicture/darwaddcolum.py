 #!/usr/bin/python3
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib 

df = pd.DataFrame(np.random.rand(10,3), columns=['Col1', 'Col2', 'Col3']) 
df['X'] = pd.Series(['A','A','A','A','A','B','B','B','B','B']) 
df['Y'] = pd.Series(['A','B','A','B','A','B','A','B','A','B']) 

plt.figure()
bp = df.boxplot(column=['Col1','Col2'], by=['X','Y']) 
plt.show()