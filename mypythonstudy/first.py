#!/usr/bin/python3
# -*- coding: UTF-8 -*-

print('Hello world!')

print(type(123))
print(type(123.0))
print(type('123'))
print(type("123"))

#判断对象是什么类型
intnum = 1000
print(isinstance(123,int))
print(isinstance(123.0,float))
print(isinstance('123',str))

print(10**1000)

a = 5
b = 10

c = a + b
print("1. c的值为:",c)

c = a - b
print("2. c的值为:",c)

c = a / b
print("3. c的值为:",c)

c = a * b
print("4. c的值为:",c)

c = a % b
print("5. c的值为:",c)

c = a ** b
print("6. c的值为:",c)

#改变 a和b的值

a = 10
b = 5

c = a // b
print("7. c的值为:",c)


a = 1
b = 1.5
c = a + b
print("8. c的值为:",c,",c的类型为：",type(c))

d = True
e = c + d
print("9. e的值为:",e,",e的类型为：",type(e))

f = 2 + 4j
g = e + f
print("10. g的值为:",g,",g的类型为：",type(g))

print("11. -1的绝对值为：", abs(-1))

print("12. 创建的复数为：", complex(1, -2))

print("13. 商和余数为：", divmod(10,3))

print("14, 浮点型转换", float(1))

print("15. 10的3次幂为：", pow(10,3))

print("16. 四舍五入为：", round(5.5))

print("17. 集合求和结果为：", sum({1,2,3,4}))

print("18. 整数20的二进制为：", bin(20))

print("19. 整数20的八进制为：", oct(20))

print("20. 整数20的十六进制为：", hex(20))

print("21. Unicode 为 97 的字符串：", chr(97))

print("22. 字符串a的Unicode码：", ord('a'))

print("23. 123的boolean值为：", bool(123))

print("24. 空字符串的 boolean的值为：", bool(''))

