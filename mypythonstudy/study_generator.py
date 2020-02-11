#!/usr/bin/python3
# -*- coding: UTF-8 -*-

list1 = [x*x for x in range(10)]
print(list1)

generator1 = (x*x for x in range(1000000000000000000000000))
print(generator1)
print(type(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
print("="*15,"next","="*15)

generator3 = (x*x for x in range(5))
for index in generator3:
    print(index)
print("="*15,"next","="*15)

def print_a(max):
    i = 0
    while i < max:
        i += 1
        yield i

a = print_a(10)
print(a)
print(type(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(a.__next__())
print(a.__next__())
print("="*15,"next","="*15)

def print_b(max):
    i = 0
    while i < max:
        i += 1
        args = yield i
        print('传入参数为：' + args)

b = print_b(20)
print(next(b))

print(b.send('Python'))