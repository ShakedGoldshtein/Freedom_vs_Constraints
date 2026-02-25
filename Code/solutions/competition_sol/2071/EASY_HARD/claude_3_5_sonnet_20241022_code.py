```python
def solve(n, points):
    def manhattan_dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def euclidean_dist(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if manhattan_dist(points[i], points[j]) == euclidean_dist(points[i], points[j]):
                count += 1
                
    # Handle coinciding points
    from collections import Counter
    x_count = Counter(x for x,y in points)
    y_count = Counter(y for x,y in points)
    
    # Add pairs of points with same x or y coordinate
    for c in x_count.values():
        if c > 1:
            count += (c * (c-1))//2
    for c in y_count.values():
        if c > 1:
            count += (c * (c-1))//2
            
    # Subtract overlapping points counted twice
    xy_count = Counter((x,y) for x,y in points)
    for c in xy_count.values():
        if c > 1:
            count -= (c * (c-1))//2
            
    return count
```