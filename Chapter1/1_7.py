# 1.7 让字典保持有序

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

'''
foo 1
bar 2
spam 3
grok 4
'''

# 比如想把数据存在json文件精确控制各字段的顺序，很简便
import json
a = json.dumps(d)

