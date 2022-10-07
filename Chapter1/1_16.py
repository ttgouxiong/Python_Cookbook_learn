# 筛选序列中的元素

mylist = [1,4,-5,10,-7,2,3,-1]
print([n for n in mylist if n>0])
# [1, 4, 10, 2, 3]

# 如果数据量大采用迭代器
pos = (n for n in mylist if n > 0)
print(pos)  # <generator object <genexpr> at 0x0000025ABCD9A5E8>

# 通过filter() 过滤生成迭代器
mylist = [1,4,-5,'ds','-',-7,2,3,-1]
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, mylist))
print(ivals)  # [1, 4, -5, -7, 2, 3, -1]

# 筛选的同时替代掉部分元素
mylist = [1,4,-5,10,-7,2,3,-1]
mylist_ = [i if i > 0 else 0 for i in mylist]
print(mylist_)  # [1, 4, 0, 10, 0, 2, 3, 0]

# itertools.compress 将布尔序列和可迭代对象作为输入，返回符合要求的新可迭代对象
address = [1,2,3,4,5,6,7,8]
count = [6,7,8,3,5,3,0,5]

from itertools import compress
more5 = [i >5 for i in count]
new_address = list(compress(address, more5))
print(new_address)  # [1, 2, 3]





