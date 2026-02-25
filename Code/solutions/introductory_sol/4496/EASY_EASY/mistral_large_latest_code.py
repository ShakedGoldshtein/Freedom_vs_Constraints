```python
def hamming_distance(a: str, b: str) -> int:
    return sum(1 for x, y in zip(a, b) if x != y)
```