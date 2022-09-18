# 1.2 从任意长度的可迭代对象中分解元素

# 很多对象需要分解，数量太大不能一一分解，多个对象可以归于一类

tt = ('aaa','bbb',1,2,3,4,5,6,7)

name1, name2, *num = tt
print(name1, name2, num)  # aaa bbb [1, 2, 3, 4, 5, 6, 7]

# 可以单独把最后一个数拿出来
name1, name2, *num, num_last = tt
print(name1, name2, num, num_last) # aaa bbb [1, 2, 3, 4, 5, 6] 7

# 对于字符串拆分 split结合起来使用也很Nice
tt = 'ttgouxiong/dsa/dsg/edfs/asd/gdf/177/139*****'
name, *_, height, phone = tt.split('/')
print(name, height, phone)   # ttgouxiong 177 139*****


