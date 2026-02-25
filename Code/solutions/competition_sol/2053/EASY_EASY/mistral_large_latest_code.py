```python
def solve(n, m, b, g):
    max_b = max(b) if b else 0
    min_g = min(g) if g else 0
    if max_b > min_g:
        return -1

    total = 0
    for bi in b:
        total += bi
    for gj in g:
        if gj > max_b:
            total += gj - max_b
    return total
```