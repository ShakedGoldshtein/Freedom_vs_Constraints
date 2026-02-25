```python
def find_remainders(T, pairs):
    results = []
    for i in range(T):
        A, B = pairs[i]
        results.append(A % B)
    return results
```