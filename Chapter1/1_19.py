# 1.19 同时对数据做转换和换算

nums = [1,2,3,4,5]
s = sum(x*x for x in nums)
print(s)     # 55

s = ('AMCME', 50, 123.45)
print(','.join(str(x) for x in s))
# AMCME,50,123.45













