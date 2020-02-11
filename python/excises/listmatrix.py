#!/usr/bin/python3
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print (matrix)

#以下实例将3X4的矩阵列表转换为4X3列表

#Funtion one
newline=[[row[i] for row in matrix] for i in range(4)]
print("\n",newline)

#Funtion two
newline = []
for i in range(4):
    newline.append([row[i] for row in matrix])
print("\n",newline)

#Funtion three
newline = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    newline_row = []
    for row in matrix:
        newline_row.append(row[i])
    newline.append(newline_row)
print("\n",newline)