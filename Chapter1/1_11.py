# 1.11 对切片命名

record = '45172483458239859843'
print(int(record[2:4]), int(record[7:8]))  # 17 3
cost = int(record[2:4]) * int(record[7:8])
print(cost)   # 51

SHARES = slice(2,4)
PRICE = slice(7,8)
print(SHARES, PRICE)   #  slice(2, 4, None) slice(7, 8, None)
print(int(record[SHARES]) * int(record[PRICE]))  # 51


items = [0,1,2,3,4,5,6]
a = slice(2,4)
items[a] = [10, 11]
print(items)   # [0, 1, 10, 11, 4, 5, 6]
del items[a]
print(items)   # [0, 1, 4, 5, 6]


a = slice(5,10)
s = 'HelloWorld'
print(a.indices(len(s)))  # (2, 4, 1)
for i in range(*a.indices(len(s))):
    print(s[i])

'''
W
o
r
l
d
'''


