```python
def min_sweets(n, m, b, g):
    b.sort()
    g.sort()
    if b[-1]>g[0]:
        return -1
    total_presents = sum(b)*(m-1) + sum(g)
    if b[-1] < g[0]:
        total_presents -= b[-1]
        total_presents += b[-2]
    return total_presents
```