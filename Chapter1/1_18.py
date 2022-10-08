# 将名称映射到序列的元素中

# 普通元组场景
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] + rec[2]
    return total

# 使用命名元组
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'prices'])
def compute_cost_new(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares + s.prices
    return total













