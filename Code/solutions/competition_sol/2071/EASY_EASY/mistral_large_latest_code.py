```python
def count_pairs(n, points):
    count = 0
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            manhattan = abs(x1 - x2) + abs(y1 - y2)
            euclidean_sq = (x1 - x2)**2 + (y1 - y2)**2
            if manhattan * manhattan == euclidean_sq:
                count += 1
    return count
```