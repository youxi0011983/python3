#!/usr/bin/python3
import pandas as pd
import os


dir = "/home/eveline/python/excel/tables"	#设置工作路径

file = os.listdir(dir)
path_file = os.path.join(dir,file[0])

df = pd.read_excel(path_file)				#打开第一个sheel
#data = df.ix[0].values						#读取第一行的内容,ix在新版取消了
data = df.loc[0].values
print("Read one line:\n{0}".format(data))
#data = df.iloc[0].values
#print("Index:\n{0}".format(data))

#返回特定行
data = df.loc[[1,2]].values
print("Read two-three line:\n{0}".format(data))

#返回指定sheel的指定行
xl = pd.ExcelFile(path_file)
sheet_name = xl.sheet_names
#print(sheet_name[0],sheet_name[1])

#data = df.loc[[1,2],[sheet_name[0],sheet_name[1]]].values
#data = df.iloc[[1,2],[sheet_name[0],sheet_name[1]]].values
#print("Read two-three line:\n{0}".format(data))

#打印行号
df=pd.read_excel(path_file)
print("输出行号列表",df.index.values)

#打印列名
df=pd.read_excel(path_file)
print("输出列标题",df.columns.values)

#获取指定行数的值：
df=pd.read_excel(path_file)
print("输出值",df.sample(3).values)#这个方法类似于head()方法以及df.values方法



#获取指定列的值：
df=pd.read_excel(path_file)
print("输出值\n",df['Supplier'].values)

firstcolum=set(df['Supplier'].values)

print("输出值集合",firstcolum)