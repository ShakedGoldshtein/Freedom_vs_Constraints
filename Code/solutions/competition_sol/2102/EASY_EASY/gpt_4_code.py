```python
def solve(k):
    edges, n = [], 0
    adjacency_mat = [[0]*100 for _ in range(100)]
    while n*(n-1)*(n-2)//6 < k:
        n += 1
    for i in range(n):
        for j in range(i):
            adjacency_mat[i][j] = 1
            adjacency_mat[j][i] = 1  
    for i in range(n-1, 0, -1):
        if n*(n-1)*(n-2)//6 - i*(i-1)*(i-2)//6 >= k:
            while n*(n-1)*(n-2)//6 - (n-1)*(n-2)*(n-3)//6 >= k:
                n -= 1
            for j in range(n, i, -1):
                adjacency_mat[i][j] = 0
                adjacency_mat[j][i] = 0
            break
    for i in range(n+1):
        edges.append(''.join(map(str, adjacency_mat[i][0:n+1])))
    return [n+1] + edges
```