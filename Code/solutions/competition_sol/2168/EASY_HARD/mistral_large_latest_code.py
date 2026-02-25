```python
def solve(n, adj_matrix, deletion_order):
    # Initialize distance matrix (Floyd-Warshall)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = adj_matrix[i][j]

    # Precompute all-pairs shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Prepare deletion order (convert to 0-based)
    x = [xi - 1 for xi in deletion_order]
    deleted = [False] * n
    result = []

    for step in range(n):
        current_x = x[step]
        deleted[current_x] = True
        total = 0

        # Calculate sum of shortest paths for remaining vertices
        remaining = []
        for v in range(n):
            if not deleted[v]:
                remaining.append(v)

        for i in range(len(remaining)):
            for j in range(len(remaining)):
                if i != j:
                    u = remaining[i]
                    v = remaining[j]
                    total += dist[u][v]

        result.append(total)

    return result
```