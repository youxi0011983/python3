# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 

while  True:
    try:
        year = int(input("输入一个年份: "))
    except ValueError:
        print("输入的不是数")
        continue

    if year == 0:
        break

    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
           else:
               print("{0} 不是闰年".format(year))
       else:
           print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
    else:
       print("{0} 不是闰年".format(year))
    print ("\n")

'''
#calendar 库中已经封装好了一个方法 isleap() 来实现这个判断是否为闰年
import calendar
print(calendar.isleap(year))
'''


