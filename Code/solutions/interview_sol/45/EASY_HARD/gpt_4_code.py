```python
def maximum_nice_stairs(t, x_values):
    results = []
    for _ in range(t):
        x = x_values[_]
        stairs = 1
        cells = 1
        while x >= cells:
            x -= cells
            stairs = stairs * 2 + 1
            cells = stairs * (stairs + 1) // 2
        results.append(_ - len(bin(stairs // 2)[2:]) + 1)
    return results
```