```python
def hamming_distance(a, b):
    return sum(e1 != e2 for e1, e2 in zip(a, b))
```