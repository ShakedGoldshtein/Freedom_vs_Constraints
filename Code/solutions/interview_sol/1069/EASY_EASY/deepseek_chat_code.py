```python
def solve(T, test_cases):
    results = []
    for i in range(T):
        A, B = test_cases[i]
        results.append(A + B)
    return results
```