```python
def robot_walk(a):
    if not a:
        return False
    
    x, y = 0, 0
    visited = {(x, y)}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    
    for move in a:
        dx, dy = directions[dir_idx]
        for _ in range(move):
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        dir_idx = (dir_idx + 1) % 4
    
    return False
```