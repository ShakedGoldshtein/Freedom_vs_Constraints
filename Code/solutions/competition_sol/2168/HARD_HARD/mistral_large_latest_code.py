```python
def solve(n, adj_matrix, deletion_order):
    # Initialize distance matrix with Floyd-Warshall
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

    # Track which vertices are still present
    present = [True] * n
    result = []

    for step in range(n):
        # Calculate current sum
        total = 0
        for v in range(n):
            if not present[v]:
                continue
            for u in range(n):
                if not present[u] or v == u:
                    continue
                total += dist[v][u]

        result.append(total)

        # Mark the next vertex as deleted
        x = deletion_order[step] - 1  # convert to 0-based
        present[x] = False

    return result
```