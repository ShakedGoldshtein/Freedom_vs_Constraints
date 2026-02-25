```python
def min_amount_spent(T, queries):
    results = []
    for i in range(T):
        N, M = queries[i]
        results.append(N * M)
    return results
```