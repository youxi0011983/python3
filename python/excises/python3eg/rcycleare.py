# -*- coding: UTF-8 -*-

# 定义一个方法来计算圆的面积
def findArea(r):
    PI = 3.142
    return PI * (r * r)


if __name__ == '__main__':
    # 调用方法
    print("圆的面积为 %.6f" % findArea(5))
