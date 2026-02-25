```python
def is_good_matrix(T, cases):
    def isValid(N, data):
        for i in range(1, N + 1):
            if data[i][i] != 0:
                return False
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                if data[i][j] != data[j][i]:
                    return False
        return True

    results = []
    for _ in range(T):
        N, Q, pairs = cases[_]
        data = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
        for pair in pairs:
            i, j, val = pair
            data[i][j] = val
            data[j][i] = val
        results.append("yes" if isValid(N, data) else "no")
    return results
```