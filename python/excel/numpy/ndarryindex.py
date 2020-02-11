#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

f = pd.Series(np.arange(5))
g = pd.Series(np.arange(5), index=np.arange(6,1,-1))
print(f)
print(g)


