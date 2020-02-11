#!/usr/bin/python3
# -*- coding: UTF-8 -*-
def print_c():
    while True:
        print('执行 A ')
        yield None
def print_d():
    while True:
        print('执行 B ')
        yield None

c = print_c()
d = print_d()
while True:
    c.__next__()
    d.__next__()