#!/usr/bin/python3
import numpy as np
import pandas as pd

#df = pd.DataFrame(pd.read_csv('name.csv',header=1))
#df = pd.DataFrame(pd.read_excel('name.xlsx'))

df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006], 
    "date":pd.date_range('20130102', periods=6), 
    "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '], 
    "age":[23,44,54,32,34,32], 
    "category":['100-A','100-B','110-A','110-C','210-A','130-F'], 
    "price":[1200,np.nan,2133,5433,np.nan,4432]},
    columns =['id','date','city','category','age','price'])

df.shape              #维度查看
df.info()               #数据表基本信息（维度、列名称、数据格式、所占空间等）
df.dtypes            #每一列数据的格式
df['date'].dtype     #某一列格式
df['price'].unique()    #查看某一列的唯一值

df.values                   #查看数据表的值
df.columns              #查看列名称
print(df.columns)

df.rename(columns={'category': 'category-size'})    #更改列名称