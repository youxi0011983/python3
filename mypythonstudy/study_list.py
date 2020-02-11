#!/usr/bin/python3
# -*- coding: UTF-8 -*-

list1 = [1, 2, 3, 4, 5]
print(list1)

list2 = ['a', 'b', 'c', 'd', 'e']
print(list2)

list3 = [1, 2, 3, 'a', 'b']
print(list3)

list4 = [1, 2.33, 'a', list3]
print(list4)

list5 = []
print(list5)

print(type(list4))

list1 = [1, 2, 3, 4, 5]
print("list1[0] is:",list1[0])

list1 = [1, 2, 3, 4, 5]
print("list1[5] is:",list1[4])

print(list1 + list2)

for i in list1:
    print(i)

print(len(list1))

print(len(list1 + list2))

print('a' in list1)
print(1 in list1)

list1 = [1, 2, 3, 4, 5]

del list1[2]
print(list1)
print("*"*30)
print(list1)
print(max(list1))
print(list4)
#print(max(list4))
print("*"*30)

print(list1)
print(min(list1))
print(list4)
#print(min(list4))
print("*"*30)


list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 省略步长时默认为 1
print("1.",list1[3:8])
# 步长为 2
print("2.",list1[3:8:2])
# 从索引 3 开始取到最后
print("3.",list1[3:])
# 从头开始取，取到索引 8 ，并且索引 8 娶不到
print("4.",list1[:8])
# 取所有，步长为 3
print("5.",list1[::3])
# 从索引 1 开始，取到倒数第 2 个，并且倒数第 2 个 取不到
print("6.",list1[1:-2])
# 取所有
print("7.",list1[:])
# 取逆序列表
print("8.",list1[::-1])
# 取逆序，并且步长为 2
print("9.",list1[8:1:-2])