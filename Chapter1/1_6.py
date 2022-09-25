# 1.6 在字典中将键映射到多个值上

# 字典的每个key对应的value为列表或者元组
d = {
    'a': [1,2,3],
    'b':[4,5]
}


# 如果手动创建会很麻烦
dd = {}
pairs = [(1,2), (1,5), (4,5)]
for key, value in pairs:
    print(key,value)
    if key not in dd:
        dd[key] = []
    dd[key].append(value)


# defaultdict会手动帮我们创建第一个值，后续添加就可以了

from collections import defaultdict

ddd = defaultdict(list)
for key, value in pairs:
    ddd[key].append(value)










