```python
def minSteps(s, t):
    from collections import Counter
    return sum((Counter(t) - Counter(s)).values())
```