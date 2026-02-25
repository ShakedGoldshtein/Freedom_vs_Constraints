```python
def count_special_pairs(n, points):
    """
    Counts the number of pairs (i, j) where 1 ≤ i < j ≤ n such that the Manhattan distance
    between points i and j equals their Euclidean distance.

    Args:
        n: Number of points (1 ≤ n ≤ 200,000).
        points: List of tuples (x, y) representing coordinates of each point.

    Returns:
        int: Number of valid pairs.
    """
    def is_special_pair(a, b):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        manhattan = dx + dy
        euclidean_sq = dx*dx + dy*dy
        return manhattan * manhattan == euclidean_sq

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if is_special_pair(points[i], points[j]):
                count += 1
    return count
```