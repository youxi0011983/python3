#!/usr/bin/python3
# -*- coding: UTF-8 -*-

list = [x for x in range(1,21)]
print("list is :",list)
print("list len is :",len(list))
print("="*15,"next","="*15)

list.append(21)
print("1. list.append(21) is:",list)
print("="*15,"next","="*15)

list.count(19)
print("2. list.count(19) is:",list)
print("="*15,"next","="*15)

list2 = [x for x in range(100,110)]
print(list2)
list.extend(list2)
print("3. list.extend(list2) is :",list)
print("="*15,"next","="*15)

list.index(102)
print("4. list.index(102) is :",list.index(103))
print("="*15,"next","="*15)

list.insert(21,999)
print("5. list.insert(21,999) is:",list)
print("="*15,"next","="*15)

list.pop()
print("6. list.pop(index=-1) is:",list)
print("="*15,"next","="*15)

list.remove(999)
print("7.list.remove(999) is :",list)
print("="*15,"next","="*15)

list.reverse()
print("8. list.reverse() is :",list.reverse())
print("list[::-1] is :",list[::-1])
print("="*15,"next","="*15)

list3 = [x for x in range(1,21)]
print("9. list3 is :", list3)
list3.sort(key=None,reverse=True)
print("list3.sort(key=None,reverse=True) is:",list3)
print("="*15,"next","="*15)


