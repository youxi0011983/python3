#!/usr/bin/python3
import pandas as pd 
import numpy as np 
import seaborn as sns
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import matplotlib

url="https://www.drugabuse.gov/sites/default/files/overdose_data_1999-2015.xls"

#读取excel表文件
overdoses = pd.read_excel(url,sheet_name='Online',skiprows=6)


#读取特定行的内容，从第二列开始。
def get_data(table,rownum,title):
	data = pd.DataFrame(table.loc[rownum][2:]).astype(float)
	data.columns = {title}
	return data 

#%matplotlib notebook		#Jupyter Notebook的 ，图表页内显示的命令

#海洛因死亡的人数读出来。这个 DataFrame 有两列，分别是年份和死亡人数。
title = 'Heroin overdoses'
d = get_data(overdoses,18,title)
x = np.array(d.index)
y = np.array(d['Heroin overdoses'])
overdose = pd.DataFrame(y,x)
overdose.columns = {title}


#接下来我们初始化一个 ffmpeg 输出流。这里我设置帧率 20 码率 1800
Write = animation.writers['ffmpeg']
write = Write(fps=20, metadata=dict(artist='Me'),bitrate=1800)

#创建图表和横纵坐标
fig = plt.figure(figsize=(10,6))
plt.xlim(1999,2016)
plt,ylim(np.min(overdose)[0],np.max(overdose)[0])
plt.xlabel('Year',fontsize=20)
plt.ylabel(title,fontsize=20)
plt.title('Heroin Overdoses per Year',fontsize=20)

def animate(i):
	data = overdose.iloc[:int(i+1)] #select data range
	p = sns.lineplot(x=data.index, y=data[title], data=data, color="r")
	p.tick_params(labelsize=17)
	plt.setp(p.lines,linewidth=7)


plt.show()

#ani = matplotlib.animation.FuncAnimation(fig,animate,frames=17,repeat=True)

#ani.save('HeroinoverdosesJump.mp4',write=write)


