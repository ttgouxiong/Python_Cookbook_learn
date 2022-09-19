# 1.3 保存最后N个元素
# 通过队列实现保存有限个元素

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)  # 这里说明了队列里面最多容纳history个数据
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


