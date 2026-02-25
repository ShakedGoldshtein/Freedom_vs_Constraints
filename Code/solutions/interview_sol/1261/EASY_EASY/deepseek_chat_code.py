```python
def solve(T, cases):
    results = []
    for N, M in cases:
        if M < N or M > N * (N - 1) // 2:
            results.append([(-1, -1)])
            continue
        
        min_edges = N
        max_edges = 2 * (N - 1) - 1
        
        if M < min_edges or M > max_edges:
            results.append([(-1, -1)])
            continue
        
        edges = []
        for i in range(1, N):
            edges.append((i, i + 1))
        edges.append((N, 1))
        
        remaining = M - N
        if remaining > 0:
            added = 0
            for i in range(1, N - 1):
                for j in range(i + 2, N + 1):
                    if added >= remaining:
                        break
                    if not (i == 1 and j == N):
                        edges.append((i, j))
                        added += 1
                if added >= remaining:
                    break
        
        results.append(edges)
    
    return results
```