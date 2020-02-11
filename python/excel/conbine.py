#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import pandas as pd
workdir = 'D:/python3/python/excel/excel_file/'
excels = [
    pd.read_excel(workdir+fname)
    for fname in os.listdir(workdir)
    if ".xlsx" in fname
]
df = pd.concat(excels)
df.to_excel("结束文件.xlsx", index=False)
