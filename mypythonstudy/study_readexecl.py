#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import xlrd
import os

os.chdir('D:/python3/mypythonstudy/test')
workbook = xlrd.open_workbook('test.xlsx')
# 输出所有 sheet 的名字
print(workbook.sheet_names())
# 获取所有的 sheet
print(workbook.sheets())
# 根据索引获取 sheet
#print(workbook.sheet_by_index(1))
# 根据名字获取 sheet
#print(workbook.sheet_by_name('1班'))
print("="*15,"next","="*15)

sheet1 = workbook.sheets()[0]
# 获取行数
print(sheet1.nrows)
# 获取列数
print(sheet1.ncols)
print("="*15,"next","="*15)

# 获取第 2 行内容
print(sheet1.row_values(1))
# 获取第 3 列内容
print(sheet1.col_values(2))
print("="*15,"next","="*15)

cell1 = sheet1.cell(1, 1).value
# 行索引
cell2 = sheet1.row(1)[1].value
cell3 = sheet1.cell(1, 2).value
# 列索引
cell4 = sheet1.col(2)[1].value
print(cell1,cell2,cell3,cell4)
print("="*15,"next","="*15)

date_value = xlrd.xldate_as_datetime(sheet1.cell_value(5, 3), workbook.datemode)
print(type(date_value), date_value)
#print(date_value)