```python
def max_total_gain(n, m, gym):
    # Precompute prefix sums for Iahub's path (top-left to bottom-right)
    iahub_prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            iahub_prefix[i][j] = gym[i-1][j-1] + max(iahub_prefix[i-1][j], iahub_prefix[i][j-1])

    # Precompute prefix sums for Iahubina's path (bottom-left to top-right)
    iahubina_prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n, 0, -1):
        for j in range(1, m + 1):
            iahubina_prefix[i][j] = gym[i-1][j-1] + max(iahubina_prefix[i+1][j] if i+1 <= n else 0,
                                                         iahubina_prefix[i][j-1])

    max_gain = 0
    # Check all possible meeting cells (i, j)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Total gain is sum of Iahub's path to (i,j) + Iahubina's path to (i,j) - gym[i-1][j-1] (since it's counted twice)
            current_gain = iahub_prefix[i][j] + iahubina_prefix[i][j] - gym[i-1][j-1]
            if current_gain > max_gain:
                max_gain = current_gain

    return max_gain
```