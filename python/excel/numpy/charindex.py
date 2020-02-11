#!/usr/bin/python3
import pandas as pd
import numpy as np

# Series是一种以为的数组型对象
a = pd.Series([9,8,7,6])
print (a)

b = pd.Series([9,8,7,6], index=['a','b','c','d'])
print (b,"\n",b.index,"\n",b.values)

print("\n",b[1])
print("\n",b['b'])
print("\n",b[['b','c','d',0]])

c = pd.Series(25, index=['a','b','c','d'])
print(c)


d = pd.Series({'a':9, 'b':8, 'c':7, 'd':6})
print(d)


e = pd.Series({'a':9, 'b':8, 'c':7, 'd':6}, index=['a','b','c','d','e'])
print(e)