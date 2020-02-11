# -*- coding: UTF-8 -*-

# Filename : factorial.py
# author : Pt

import math
from time import *

start = time()

num = int(input("请输入一个数字："))
if num < 0:
    print("负数是没有阶乘的！")
else:
    print("{0} 的阶乘为 {1}".format(num, math.factorial(num)))

elapsed = (time() - start)
print("Time used:",elapsed)