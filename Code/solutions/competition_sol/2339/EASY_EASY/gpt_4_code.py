```python
def solve(t, test_cases):
    results = []
    for i in range(t):
        n, a, b = test_cases[i]
        operations = []
        a, b = list(a), list(b)
        for j in range(n-1, -1, -1):
            if a[j] == b[j]:
                continue
            if a[0] == b[j]:
                a = a[::-1]
                operations.append(n)
            a[0] = b[j]
            a = a[::-1]
            operations.append(n-j)
        results.append((len(operations), operations))
    return results
```
Here `test_cases` is assumed to be a list of triples, where each triple represents one test case. Each triple is a tuple `(n, a, b)`, where `n` is the length of the binary strings, and `a` and `b` are the binary strings themselves.

The function `solve` returns a list of test case results, where each result is a tuple `(k, operations)`. Here `k` is the number of operations, and `operations` is the list of prefix lengths that were flipped.