#!/usr/bin/python3
import time

n=int(input('请输入一个整数:'))
a=0
b=1
start = time.time()
def F(n,a,b):
 if n==0:
    return a
 return F(n-1,b,a+b)
print(F(n,a,b))
end = time.time()
print("运行时间:%.2f秒"%(end-start))