```python
from collections import defaultdict

def solve(n, coords):
    x_coords = defaultdict(int)
    y_coords = defaultdict(int)
    points = defaultdict(int)
    for i in range(n):
        x, y = coords[i]
        x_coords[x] += 1
        y_coords[y] += 1
        points[(x, y)] += 1
    result = 0
    for val in x_coords.values():
        result += val * (val - 1) // 2
    for val in y_coords.values():
        result += val * (val - 1) // 2
    for val in points.values():
        result -= val * (val - 1) // 2
    return result

```
