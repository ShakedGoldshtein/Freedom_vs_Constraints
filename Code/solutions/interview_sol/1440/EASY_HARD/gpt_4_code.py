```python
def max_cost(T, tests):
    result = []
    for i in range(T):
        N = tests[i][0]
        A = sorted(tests[i][1], reverse=True)
        extra = A[1:]
        cost = A[0]
        for j in range(N - 3, -1, -1):
            cost = cost % extra[j]
        cost = cost % A[0]
        result.append(cost)
    return result
```