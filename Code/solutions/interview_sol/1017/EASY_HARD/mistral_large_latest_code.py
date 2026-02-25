```python
def solve(test_cases):
    results = []
    for case in test_cases:
        A1, A2, A3, A4, A5, P = case
        total_work = A1 * P + A2 * P + A3 * P + A4 * P + A5 * P
        total_available = 5 * 24
        results.append("Yes" if total_work > total_available else "No")
    return results
```