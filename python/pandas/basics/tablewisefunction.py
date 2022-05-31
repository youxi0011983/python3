#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import statsmodels.formula.api as sm
import pandas as pd

bb = pd.read_csv('data/baseball.csv', index_col='id')

(bb.query('h > 0')
   .assign(ln_h=lambda df: np.log(df.h))
   .pipe((sm.ols, 'data'), 'hr ~ ln_h + year + g + C(lg)')
   .fit()
   .summary()
 )
