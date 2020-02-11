#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from collections.abc import Iterable

print(isinstance('geekdigging', Iterable))
print(isinstance([], Iterable))
print(isinstance([], Iterable))
print(isinstance({x for x in range(5)}, Iterable))
print(isinstance(123, Iterable))

list1 = [1, 2, 3, 4]
list1 = iter(list1)
print(type(list1))
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))