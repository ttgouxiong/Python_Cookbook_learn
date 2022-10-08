# 1.20 将多个映射合并为单个映射

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

# 重复的键会采用第一个映射中的值
from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])  # 1
print(c['y'])  # 2
print(c['z'])  # 3

# 修改的操作总会作用于第一个映射结构上
del c['x']
print(c)  # ChainMap({'z': 3}, {'y': 2, 'z': 4})
del c['y']  # KeyError: 'y'












