#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

a = pd.Series([1,1,1,np.nan],index=['a','b','c','d'])
print (a)

b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
print(b)

print(a.add(b,fill_value=0))
print (a)