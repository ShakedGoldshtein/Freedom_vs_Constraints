```python
from collections import Counter

def minSteps(s, t):
    count_s = Counter(s)
    count_t = Counter(t)
    
    diff = 0
    for char in count_s:
        if count_s[char] > count_t[char]:
            diff += count_s[char] - count_t[char]
    
    return diff
```