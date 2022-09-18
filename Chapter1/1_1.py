# 序列分解为连续的变量
p = (3,5)
x,y = p

print(x, y)  # 3,5

# 可迭代对象都可以做分解操作

# 可以用用不到的变量名字来丢弃部分值
tt = 'abcde'
_, b, c, d, _ = tt
print(b, c, d)   # b c d
