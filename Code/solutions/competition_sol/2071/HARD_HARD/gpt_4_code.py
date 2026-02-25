```python
from collections import Counter
from math import factorial

def nCr(n):  
    return factorial(n)//(factorial(2)*factorial(n-2))

def solve(n, watchers):
    x = Counter([i[0] for i in watchers])
    y = Counter([i[1] for i in watchers])
    xy = Counter(watchers)
    
    total = 0
    for k in x.values():
        if k > 1:
            total += nCr(k)
    for k in y.values():
        if k > 1:
            total += nCr(k)
    for k in xy.values():
        if k > 1:
            total -= nCr(k)
            
    return total
```