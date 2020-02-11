#!/usr/bin/python3
import time


#计算递归斐波那契时间消耗
n=int(input('请输入一个整数:'))
start = time.time()
def fab(n):
    if n<1:
        print('输入有误！')
        return -1    
    if n==1 or n==2:
        return 1    
    else:
        return fab(n-1)+fab(n-2)
print(fab(n))
end = time.time()
print("运行时间:%.2f秒"%(end-start))
#计算两个变量时间消耗
start = time.time()
a, b = 0, 1
cn = 1
while cn < n:
    a, b = b, a+b
    cn += 1
print(b)
end = time.time()
print("运行时间:%.2f秒"%(end-start))