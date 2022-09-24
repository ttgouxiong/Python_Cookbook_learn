# 1.5实现优先级队列


import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# 例子
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())   # Item('bar')
print(q.pop())  # Item('spam')



# Item实例是没法比较大小的
a = Item('foo')
b = Item('bar')
# print(a<b)
'''
Traceback (most recent call last):
  File "D:/Python_Cookbook_learn/Chapter1/1_5.py", line 41, in <module>
    a<b
TypeError: '<' not supported between instances of 'Item' and 'Item'
'''


# 但是元组之间可以比较
aa = (1, Item('foo'))
bb = (4, Item('bar'))
print(aa<bb)   # True
# 但是优先级一样也会报错
cc = (1, Item('lal'))
# print(aa<cc)
'''
Traceback (most recent call last):
  File "D:/Python_Cookbook_learn/Chapter1/1_5.py", line 41, in <module>
    a<b
TypeError: '<' not supported between instances of 'Item' and 'Item'
'''

# 通过引入额外索引解决问题
aaa = (1, 0, Item('foo'))
bbb = (4, 1, Item('bar'))
ccc = (1, 2, Item('bar'))
print(aaa<bbb)    # True
print(aaa<ccc)    # True