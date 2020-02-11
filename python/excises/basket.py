#!/usr/bin/python3

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}


print(basket)                          # 删除重复的

if 'orange' in basket:               # 检测成员
    print(True)
else:
    print(False)

if 'crabgrass' in basket:
    print(True)
else:
    print(False)

# 以下演示了两个集合的操作
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # a 中唯一的字母
print(a-b)                              # 在 a 中的字母，但不在 b 中
print(a | b)                            # 在 a 或 b 中的字母
print(a & b)                          # 在 a 和 b 中都有的字母
print(a ^ b)                            # 在 a 或 b 中的字母，但不同时在 a 和 b 中