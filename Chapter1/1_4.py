# 1.4 找到最大或最小的N个元素

import heapq
nums = [1,7,2,34,7,-5, 32,5,33]
print(heapq.nlargest(3,nums))   # [34, 33, 32]
print(heapq.nsmallest(3,nums))   # [-5, 1, 2]

heapq.heapify(nums)
print(nums)  # [-5, 5, 1, 7, 7, 2, 32, 34, 33]

print(heapq.heappop(nums))  # -5
print(heapq.heappop(nums))  #  1
print(heapq.heappop(nums))  #  2




