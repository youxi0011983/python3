#!/usr/bin/python3
# -*- coding: UTF-8 -*-


dict1 = {'name': 'geekdigging', 'age': 2}
print(dict1)
print(type(dict1))

dict2 = {(1, 2, 3): '123', 'name': 'geekdigging', 2: [1, 2, 3]}
print(dict2)
print(type(dict2))

str = 'geekdigging'

if str in dict1:
    print(dict1['geekdigging'])
else:
    print('您查询的键', str, '不存在')

# 添加
dict1['a'] = 18
print(dict1)
# 更新
dict1['name'] = 'www.geekdigging.com'
print(dict1)
# 删除
del dict1['a']
print(dict1)

print("="*15,"next","="*15)
#返回一个迭代器，可以使用 list() 来转换为列表，该列表包含所有的 key。
dict1 = {'name': 'geekdigging', 'age': 2}

print(dict1.keys())
print(list(dict1.keys()))
print(type(list(dict1.keys())))

print(dict1.values())
print(list(dict1.values()))
print(type(list(dict1.values())))

print(dict1.items())
print(list(dict1.items()))
print(type(list(dict1.items())))

print(dict1.get('name'))
print(dict1.get('geekdigging'))

print(dict1.pop('age'))
print(dict1)

dict1.setdefault('age')
print(dict1)

dict2 = {'sex': 'male'}
dict1.update(dict2)
print(dict1)