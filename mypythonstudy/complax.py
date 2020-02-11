#!/usr/bin/python3
# -*- coding: UTF-8 -*-

a = 5
b = 10

if (a == b):
    print("25. a 等于 b")
else:
    print("25. a 不等于 b")

if (a != b):
    print("26. a 不等于 b")
else:
    print("26. a 等于 b")

if (a < b):
    print("27. a 小于 b")
else:
    print("27. a 大于等于 b")

if (a > b):
    print("28. a 大于 b")
else:
    print("28. a 小于等于 b")

if (a <= b):
    print("29. a 小于等于 b")
else:
    print("29. a 大于  b")

if (b >= a):
    print("30. b 大于等于 a")
else:
    print("30. b 小于 a")


a = 10
b = 20

c = a + b
print("c = a + b 的值为：", c)

c += a
print("c += a 的值为：", c)

c *= a
print("c *= a 的值为：", c)

c /= a
print("c /= a 的值为：", c)

c = 2
c %= a
print("c %= a 的值为：", c)

c **= a
print("c **= a 的值为：", c)

c //= a
print("c //= a 的值为：", c)