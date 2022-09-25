# 1.9 在两个字典中寻找相同点

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 12,
    'x': 22,
    'y': 2
}

# 去除key或者value，之后做集合操作即可
print(a.keys() & b.keys())  #  {'x', 'y'}
print(a.keys() - b.keys())  #  {'z'}
print(a.items() & b.items())  #  {('y', 2)}

# 移除字典里面的某些内容
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)  #  {'y': 2, 'x': 1}









