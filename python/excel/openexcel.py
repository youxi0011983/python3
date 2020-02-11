#!/usr/bin/python3
import pandas as pd
import os

dir = "/home/eveline/python/excel/tables"#设置工作路径

#新建列表，存放文件名（可以忽略，但是为了做的过程能心里有数，先放上）
filename_excel = []

#新建列表，存放每个文件数据框（每一个excel读取后存放在数据框）
frames = []

#找到目录下的文件返回文件名字和路径
files=os.listdir(dir)
path_file = os.path.join(dir,files[0]) 
print(path_file)

#方法一：通过指定表单名的方式来读取
df = pd.read_excel(path_file)
data = df.head()					#显示前五行的内容
#data = df.values					#显示全部内容
#print("Recvie:\n{0}".format(data))


#方法二：通过指定表单名的方式来读取
#df=pd.read_excel(path_file,sheet_name='student')#可以通过sheet_name来指定读取的表单
#data=df.head()#默认读取前5行的数据
#print("获取到所有的值:\n{0}".format(data))#格式化输出


#方法三：通过表单索引来指定要访问的表单，0表示第一个表单
#也可以采用表单名和索引的双重方式来定位表单
#也可以同时定位多个表单，方式都罗列如下所示
#df=pd.read_excel(path_file,sheet_name=['python','student'])#可以通过表单名同时指定多个
# df=pd.read_excel('lemon.xlsx',sheet_name=0)#可以通过表单索引来指定读取的表单
# df=pd.read_excel('lemon.xlsx',sheet_name=['python',1])#可以混合的方式来指定
# df=pd.read_excel('lemon.xlsx',sheet_name=[1,2])#可以通过索引 同时指定多个
#data=df.values#获取所有的数据，注意这里不能用head()方法哦~
#print("获取到所有的值:\n{0}".format(data))#格式化输出

#返回表单的名字
xl = pd.ExcelFile(path_file)
sheet_name = xl.sheet_names
print(sheet_name)

df = pd.read_excel(path_file,None);
print(df.keys())

#返回所有sheel数据
#方法一
#df = xl.parse(sheet_name)
#print(df)

#方法二
#df = pd.read_excel(path_file,None);