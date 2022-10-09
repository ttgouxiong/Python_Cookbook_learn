# 2.1 针对任意多的分隔符拆分字符串

# 对于字符串有多个分隔符的时候split无法满足要求

import re
line = 'asdf fjdk; afed, fjek,asdf,   foo'
line_split = re.split(r'[;,\s]\s*', line)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 正则表达式中的捕获组
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)









