# 1.8 与字典有关的计算问题

prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))   # (10.75, 'FB')
# 因为zip()创建了一个迭代器，他的内容只能被消费一次，所以下面再次使用会报错
print(max(prices_and_names))   # ValueError: max() arg is an empty sequence

price_sorted = sorted(zip(prices.values(), prices.keys()))
print(price_sorted)  # [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]


# 对字典的数据操作往往是对key值的操作
print(min(prices))  # AAPL
print(max(prices))   # IBM
# 这往往不是我们想要的，可以对values排序
print(max(prices.values()))  # 612.78
# 但是我们还想知道key相关的信息。可以传递一个key参数给 min/max, 但是还要到字典里面二次查找一下
min_value = prices[min(prices, key=lambda k:prices[k])]
print(min(prices, key=lambda k:prices[k]), min_value)   # FB 10.75

# 用zip反转键和值，解决问题
print(min(zip(prices.values(), prices.keys())))  #(10.75, 'FB')

