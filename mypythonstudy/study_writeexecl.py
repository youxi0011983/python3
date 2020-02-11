#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import xlsxwriter
import os
import datetime

os.chdir('D:/python3/mypythonstudy/test')
workbook = xlsxwriter.Workbook('demo.xlsx')

sheet1 = workbook.add_worksheet('test_sheet')


workfomat = workbook.add_format()
# 字体加粗
workfomat.set_bold(True)
# 单元格边框宽度
workfomat.set_border(1)
# 对齐方式
workfomat.set_align('left')
# 格式化数据格式为小数点后两位
workfomat.set_num_format('0.00')

heads = ['', '语文', '数学', '英语']
datas = [
    ['小明', 76, 85, 95],
    ['小红', 85, 58, 92],
    ['小王', 98, 96, 91]
]

sheet1.write_row('A1', heads, workfomat)

sheet1.write_row('A2', datas[0], workfomat)
sheet1.write_row('A3', datas[1], workfomat)
sheet1.write_row('A4', datas[2], workfomat)
fomat1 = workbook.add_format({'num_format': 'yy/mm/dd/ hh:mm:ss'})

sheet1.write_datetime('E5', datetime.datetime(2019, 11, 9, 22, 44, 26), fomat1)
# 字符串类型
#sheet1.write_string()
# 数字型
#sheet1.wirte_number()
# 空类型
#sheet1.write_blank()
# 公式
#sheet1.write_formula()
# 布尔型
#sheet1.write_boolean()
# 超链接
#sheet1.write_url()
#sheet1.insert_image('I6', 'wx.jpg')
'''
insert_image(row, col, image[, options])

row：行坐标，起始索引值为0；
col：列坐标，起始索引值为0；
image：string类型，是图片路径；
options：dict类型，是可选参数，用于指定图片位置，如URL等信息；
'''
#我们还可以在 Excel 中绘图，支持包括面积、条形图、柱状图、折线图、散点图等。

#图表对象是通过 Workbook add_chart() 方法创建的，其中指定了图表类型：

#chart = workbook.add_chart({'type': 'column'})

'''
area：面积样式的图表
bar：条形图
column：柱状图
line：线条样式的图表
pie：饼形图
scatter：散点图
stock：股票样式的图表
radar：雷达样式的图表
'''
#sheet1.insert_chart('A7', chart)

chart = workbook.add_chart({'type': 'column'})

chart.add_series({'values': '=test_sheet!$B$2:$B$4'})
chart.add_series({'values': '=test_sheet!$C$2:$C$4'})
chart.add_series({'values': '=test_sheet!$D$2:$D$4'})

sheet1.insert_chart('A7', chart)
workbook.close()
