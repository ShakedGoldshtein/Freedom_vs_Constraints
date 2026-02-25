```python
def minimum_amount(T, nm_values):
    min_amounts = []
    for i in range(T):
        N, M = nm_values[i]
        min_amounts.append(N*M)
    return min_amounts
```