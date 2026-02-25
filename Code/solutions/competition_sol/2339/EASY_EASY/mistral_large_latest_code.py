```python
def solve(test_cases):
    results = []
    for case in test_cases:
        n, a, b = case
        operations = []
        current = list(a)
        for i in range(n-1, -1, -1):
            if current[i] != b[i]:
                operations.append(i+1)
                for j in range(i+1):
                    current[j] = '1' if current[j] == '0' else '0'
                current[:i+1] = current[:i+1][::-1]
        results.append((len(operations), operations))
    return results
```