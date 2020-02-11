#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import os
import re

#设置文件的路径
dir = "/home/eveline/python/excel/tables"

#新建列表，存放文件名（可以忽略，但是为了做的过程能心里有数，先放上）
filename_excel = []
#新建列表，存放每个文件数据框（每一个excel读取后存放在数据框）
frames = []



#查看目录下文件名，是否是excel文件
pattern = r'.*(xlsx|xls)$'

for root, dirs, files in os.walk(dir):
	for file in files:
		matchexcelfile = re.match(pattern,file)
		if matchexcelfile == None:
			exit()
		filename_excel.append(os.path.join(root,file))
		df = pd.read_excel(os.path.join(root,file))#excel转换成DataFrame+
		for char in df.columns:
			df.rename(columns={char: char.lower()})
		frames.append(df)

#print (frames)

#合并所有数据
result = pd.concat(frames,axis = 0,ignore_index = True)


combinefile = 'a12.xlsx'
combinesheetname = 'new'

#输出到文件
result.to_excel(combinefile)