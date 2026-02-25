```python
def solve(k):
    n = 0
    while n * (n - 1) * (n - 2) // 6 < k:
        n += 1
        if n > 100:
            break
    
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            adj[i][j] = 1
            adj[j][i] = 1
    
    current = n * (n - 1) * (n - 2) // 6
    extra = n
    while current > k and extra < 100:
        remove_from = n - 1
        while remove_from >= 2 and current > k:
            if current - remove_from * (remove_from - 1) // 2 >= k:
                current -= remove_from * (remove_from - 1) // 2
                for i in range(remove_from):
                    adj[i][extra] = 0
                    adj[extra][i] = 0
                extra += 1
            else:
                remove_from -= 1
    
    while current > k:
        for i in range(n - 1, 1, -1):
            if current - i * (i - 1) // 2 >= k:
                current -= i * (i - 1) // 2
                for j in range(i):
                    adj[j][n] = 0
                    adj[n][j] = 0
                n += 1
                break
    
    result = []
    result.append(str(n))
    for i in range(n):
        result.append(''.join(str(adj[i][j]) for j in range(n)))
    return '\n'.join(result)
```