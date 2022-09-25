# 1.12 找出序列中出现 次数最多的元素

from collections import Counter
nums = [1,5,2,4,2,65,3,21,21,3,2,4,3,4,2,4]
num_counts = Counter(nums)
top_three = num_counts.most_common(3)
print(top_three)  # [(2, 4), (4, 4), (3, 3)]

print(num_counts[3])   # 3

# Counter可以同各种运算符结合使用
nums_a = [1,5,2,4,2,65,3,21,21,3,2,4,3,4,2,4]
nums_b = [1,5,2,4,4,5,3,2,3,4,2,4]
print(Counter(nums_a))   # Counter({2: 4, 4: 4, 3: 3, 21: 2, 1: 1, 5: 1, 65: 1})
print(Counter(nums_b))   # Counter({4: 4, 2: 3, 5: 2, 3: 2, 1: 1})
print(Counter(nums_a) + Counter(nums_b))  # Counter({4: 8, 2: 7, 3: 5, 5: 3, 1: 2, 21: 2, 65: 1})
print(Counter(nums_a) - Counter(nums_b))  # Counter({21: 2, 2: 1, 65: 1, 3: 1})









