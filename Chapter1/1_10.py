# 1.10 从序列中移除重复项且保持元素间顺序不变

# 对于可哈希对象
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,5,2,1,9,1,5,10]
print(list(dedupe(a)))  # [1, 5, 2, 9, 10]

# 对于不可哈希对象
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)

        if val not in seen:
            yield item
            seen.add(val)

a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe2(a, key=lambda t:(t['x'], t['y']))))
#[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]

# 如果只是简单的去重，可以用集合set，但是结果可能会被打乱
a = [1,5,2,1,9,1,5,10]
print(set(a))  #{1, 2, 5, 9, 10}