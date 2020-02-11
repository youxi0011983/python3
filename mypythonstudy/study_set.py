#!/usr/bin/python3
# -*- coding: UTF-8 -*-

set1 = {1, 2, 3, 'Python', (1, 'geekdigging')}
print(set1)
print(type(set1))

# 演示不可重复
set2 = {1, 2, 2}
print(set2)

# 演示空集合
set3 = set()
print(set3)
print(type(set3))

# 使用 list 创建集合
list1 = [1, 1, 2, 2, 3, 4]
set4 = set(list1)
print(set4)

# 使用 tuple 创建集合
tup1 = (1, 1, 2, 2, 3, 4)
set5 = set(tup1)
print(set5)

# 使用字符串创建集合
str1 = 'geekdigging'
set6 = set(str1)
print(set6)
print("="*15,"next","="*15)


set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 7, 9}

# 求交集
set3 = set1.intersection(set2)
print('交集：', set3)

# 求并集
set4 = set1.union(set2)
print('并集：', set4)

# 做差
set5 = set1.difference(set2)
print('做差：', set5)
print("="*15,"next","="*15)

set6 = {1, 2, 3}
set6.add(4)
print(set6)
set6.add('python')
print(set6)
set6.add((1, 2))
print(set6)
print("="*15,"next","="*15)

set7 = {1, 2}
set7.update({3, 4, 'python', (4, 5)})
print(set7)
set7.pop()
print(set7)
print("="*15,"next","="*15)

set8 = {1, 2, 3, 4}
set8.remove(4)
print(set8)
set8.discard(9)
print(set8)
set9 = {1, 2, 3}
set9.clear()
print(set9)
print("="*15,"next","="*15)

#判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
set10 = {1, 2, 3}
set11 = {1, 2}
set12 = {4, 5}
print(set10.isdisjoint(set11))
print(set10.isdisjoint(set12))
print("="*15,"next","="*15)

#作用：判断指定集合是否为该方法参数集合的子集。
print(set11.issubset(set10))
print(set12.issubset(set10))


#作用：判断该方法的参数集合是否为指定集合的子集。
print(set10.issuperset(set11))
print(set10.issuperset(set12))
