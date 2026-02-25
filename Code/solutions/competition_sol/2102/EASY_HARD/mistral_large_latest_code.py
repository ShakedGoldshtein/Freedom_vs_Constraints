```python
def construct_graph(k):
    if k == 1:
        n = 3
        adj = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
    else:
        n = 5
        adj = [
            [0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0]
        ]
        total = 10
        if k <= total:
            pass
        else:
            m = (k + 9) // 10
            n = 3 + m
            adj = [[0] * n for _ in range(n)]
            for i in range(3):
                for j in range(3):
                    if i != j:
                        adj[i][j] = 1
            for i in range(3, n):
                adj[i][i] = 0
                for j in range(3):
                    adj[i][j] = 1
                    adj[j][i] = 1
    return (n, adj)
```