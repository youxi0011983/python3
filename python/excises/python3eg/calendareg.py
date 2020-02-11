#!/usr/bin/python3
# Filename : test.py
# author by : www.runoob.com
 
# 引入日历模块
import calendar
 
# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))
 
#设置第一天是星期天
calendar.setfirstweekday(firstweekday=6)

# 显示日历
print(calendar.month(yy,mm))

print(calendar.calendar(yy))