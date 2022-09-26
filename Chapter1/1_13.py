# 1.13 通过公共键对字典列表排序，运用operator中的itemgetter

rows = [
    {'name':'dabao', 'age':5},
    {'name': 'abao', 'age': 3},
    {'name': 'jubao', 'age': 1},
    {'name': 'anbao', 'age': 2}
]


from operator import itemgetter
rows_by_name = sorted(rows, key=itemgetter('name'))
rows_by_age = sorted(rows, key=itemgetter('age'))
print(rows_by_name)
# [{'name': 'abao', 'age': 3}, {'name': 'anbao', 'age': 2}, {'name': 'dabao', 'age': 5}, {'name': 'jubao', 'age': 1}]
print(rows_by_age)
# [{'name': 'jubao', 'age': 1}, {'name': 'anbao', 'age': 2}, {'name': 'abao', 'age': 3}, {'name': 'dabao', 'age': 5}]
# 先按照名字再按照年龄
rows_by_name_age = sorted(rows, key=itemgetter('name', 'age'))
print(rows_by_name_age)
# [{'name': 'abao', 'age': 3}, {'name': 'anbao', 'age': 2}, {'name': 'dabao', 'age': 5}, {'name': 'jubao', 'age': 1}]



