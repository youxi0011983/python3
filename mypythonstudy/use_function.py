#!/usr/bin/python3
# -*- coding: UTF-8 -*-

Position_number=0
def a():#第一层函数
    global Position_number
    def b():#第二层函数
        print('打开文件B')
    def c():
        print('打开文件C')
    def d():
        print('打开文件D')
    if(Position_number==0):
        return(b)
    if(Position_number==1):
        return(c)
    if(Position_number==2):
        return(d)
s=a()                   #首先要调用一次a函数，将a函数的返回值给s，这里也就是b函数
s()                     #运行b函数
Position_number=1       #改变Position_number，使a()的返回值改变成c函数
s=a()                   #将c函数赋给s
s()                     #运行c函数
Position_number=2       #改变Position_number，使a()的返回值改变成c函数
s=a()                  #将d函数赋给s
s()                    #运行d函数
