```python
def solve(test_cases):
    result = []

    for test_case in test_cases:
        N, Q, queries = test_case
        matrix = [[-1] * N for _ in range(N)]
        possible = True

        for query in queries:
            i, j, val = query
            if matrix[j-1][i-1] != -1 and matrix[j-1][i-1] != val:
                possible = False
                break
            matrix[i-1][j-1] = val
            matrix[j-1][i-1] = val
            if i != j:
                matrix[i-1][i-1] = 0
                matrix[j-1][j-1] = 0
            if val == 1 and (matrix[i-1][i-1] != 0 or matrix[j-1][j-1] != 0):
                possible = False
                break

        result.append('yes' if possible else 'no')

    return result
```
