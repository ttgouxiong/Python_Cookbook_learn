# 2.2 在字符串的开头或结尾处做文本匹配

filename = 'spam.txt'
print(filename.endswith('.txt')) # True

import os
filename = os.listdir('.')
print(filename)  # ['2_1.py', '2_2.py']
filename_list = [name for name in filename if name.endswith('.py')]
print(filename_list)  # ['2_1.py', '2_2.py']












