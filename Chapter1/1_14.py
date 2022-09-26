# 1.14 对不原生支持比较操作的对象排序

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print(users)  # [User(23), User(3), User(99)]

a = sorted(users, key=lambda t:t.user_id)
print(a)  #  [User(3), User(23), User(99)]


# 也可以用operator.attrgetter方法实现

from operator import attrgetter
a = sorted(users, key=attrgetter('user_id'))
print(a)  # [User(3), User(23), User(99)]



