# 1.15 根据字段将记录分组

rows = [
    {'name':'sda', 'money':23},
    {'name': 'sd232a', 'money': 2},
    {'name': 'sd6yrta', 'money': 233},
    {'name': 'sdwera', 'money': 233},
    {'name': 'sdya', 'money': 23},
    {'name': 'sdegta', 'money': 23},
    {'name': 'sddsa', 'money': 2},
    {'name': 'sewda', 'money': 2},
]

from operator import itemgetter
from itertools import groupby

# 先以目标字段进行排序（不然后续结果会出现重复的情况，groupby只检查连续的项）
rows.sort(key=itemgetter('money'))

# 再分组操作
for money, items in groupby(rows, key=itemgetter('money')):
    print(money)
    for i in items:
        print('  ', i)

'''
2
   {'name': 'sd232a', 'money': 2}
   {'name': 'sddsa', 'money': 2}
   {'name': 'sewda', 'money': 2}
23
   {'name': 'sda', 'money': 23}
   {'name': 'sdya', 'money': 23}
   {'name': 'sdegta', 'money': 23}
233
   {'name': 'sd6yrta', 'money': 233}
   {'name': 'sdwera', 'money': 233}
'''


# 也可以使用1.6学到的defaultdic方法直接按照类存放
from collections import defaultdict
rows_by_money = defaultdict(list)
for row in rows:
    rows_by_money[row['money']].append(row)
# 这样可以直接访问每个money下的元素
print(rows_by_money[233])
#  [{'name': 'sd6yrta', 'money': 233}, {'name': 'sdwera', 'money': 233}]


