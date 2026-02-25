```python
from bisect import bisect_right, bisect_left, insort
from collections import deque

def array_weight(n, q, a, queries):
    res = [0]*q
    b = [0]*(n+5)
    b[-1] = n+5
    pos = deque()
    for i in range(n-1, -1, -1):
        b[bisect_left(b, a[i]) - 1] = a[i]
        pos.appendleft(bisect_right(b, 0, 0, n+2) - 1)
    for i in range(q):
        x,y = queries[i]
        res[i] = pos[bisect_right(pos, n-y, 0, n-x)]
    return res

#example usage with the two provided input examples
print(array_weight(13, 5, [2, 2, 3, 9, 5, 4, 6, 5, 7, 8, 3, 11, 13], [(3, 1), (0, 0), (2, 4), (5, 0), (0, 12)]))
print(array_weight(5, 2, [1, 4, 1, 2, 4], [(0, 0), (1, 0)]))
```