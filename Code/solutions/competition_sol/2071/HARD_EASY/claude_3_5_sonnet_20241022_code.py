```python
from collections import defaultdict
from math import sqrt

def manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def euclidean_dist(x1, y1, x2, y2): 
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def solve(n, points):
    result = 0
    
    # Handle coinciding points
    point_counts = defaultdict(int)
    for x, y in points:
        point_counts[(x,y)] += 1
        
    # Add pairs of coinciding points
    for count in point_counts.values():
        if count > 1:
            result += (count * (count-1)) // 2
            
    # Check all other point pairs
    points = list(point_counts.keys())
    m = len(points)
    
    for i in range(m):
        for j in range(i+1, m):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            manh = manhattan_dist(x1, y1, x2, y2)
            eucl = euclidean_dist(x1, y1, x2, y2)
            
            if abs(manh - eucl) < 1e-9:
                mult = point_counts[(x1,y1)] * point_counts[(x2,y2)]
                result += mult
                
    return result
```