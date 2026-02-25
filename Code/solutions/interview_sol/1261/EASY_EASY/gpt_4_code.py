```python
def solve(T, tests):
    results = []
    for N, M in tests:
        if M < N-1 or M > N*(N-1)//2:
            results.append((-1, -1))
        else:
            res = []
            for i in range(1,N+1):
                res.append((i%(N)+1, (i+1)%(N)+1))
            remaining = M - N
            if remaining > 0:
                for i in range(2,N):
                    for j in range(i+2, min(N+1, i+remaining+1)):
                        res.append((i, j))

            results.append(res[:M])
    return results

print(solve(2, [(10, 1), (5, 5)]))
```
