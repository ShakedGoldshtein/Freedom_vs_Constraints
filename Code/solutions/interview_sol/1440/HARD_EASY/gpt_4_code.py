```python
def max_cost_ordering(testcases):
    result = []
    for testcase in testcases:
        N, A = testcase
        A.sort()
        cost = A[-2]
        for i in range(N-3, -1, -1):
            cost = cost % A[i]
        result.append(cost)
    return result
```