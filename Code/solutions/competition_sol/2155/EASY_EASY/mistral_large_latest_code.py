```python
def max_gain(n, m, a):
    # Precompute prefix sums for Iahub's paths (top-left to bottom-right)
    prefix_iahub = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_iahub[i][j] = a[i-1][j-1] + max(prefix_iahub[i-1][j], prefix_iahub[i][j-1])

    # Precompute prefix sums for Iahubina's paths (bottom-left to top-right)
    prefix_iahubina = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n, 0, -1):
        for j in range(1, m + 1):
            prefix_iahubina[i][j] = a[i-1][j-1] + max(prefix_iahubina[i+1][j], prefix_iahubina[i][j-1])

    max_total = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1 and j == 1) or (i == n and j == 1) or (i == 1 and j == m) or (i == n and j == m):
                continue  # Cannot be meeting point (start/end points)
            current = prefix_iahub[i][j] + prefix_iahubina[i][j] - a[i-1][j-1]
            if current > max_total:
                max_total = current

    return max_total
```