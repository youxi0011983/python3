#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def add(a,b):
    return  a + b

if __name__ in '__main__':
    print(add(1,2))
print("="*15,"next","="*15)

#参数 b 前面加一个 * ，表示这个参数是可变长参数，当前面的参数都赋值结束后，剩下的参数顺次给这个参数赋值
def print_a(a, *b):
    print(a, b)
print_a(1, 2, 3, 4, 5, 6)
print("="*15,"next","="*15)

#参数前面加两个 * ，表示这个参数可以传递的数据类型是以字典的形式传递的
def print_b(a, **b):
    print_a(a, b)
print_b(1, q='q', w='w', e='e')
print("="*15,"next","="*15)

print_a(1)
print_b(1)
print("="*15,"next","="*15)

a = 0

def print_1():
    a = 1
    print('a1 =', a)

    def print_2():
        a = 2
        print('a2 =', a)
    print_2()

print('a3 =', a)
print_1()
print('a =', a)

print("="*15,"next","="*15)

a = 0

def print_1():
    # a = 1
    print('a1 =', a)

    def print_2():
        a = 2
        print('a2 =', a)

    print_2()

print('a3 =', a)
print_1()
print('a =', a)
print("="*15,"next","="*15)

add = lambda x,y: x + y

print(add(1, 2))
