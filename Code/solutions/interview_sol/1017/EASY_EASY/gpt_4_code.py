```python
def solve(T, test_cases):
    results = []
    for i in range(T):
        A = test_cases[i][:-1]
        P = test_cases[i][-1]
        if sum(A) * P > 120:
            results.append("Yes")
        else:
            results.append("No")
    return results
```