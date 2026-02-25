```python
def robot_path_crosses(a):
    visited = set()
    x, y = 0, 0
    direction = 0  # 0: up, 1: right, 2: down, 3: left
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited.add((x, y))

    for step in a:
        dx, dy = directions[direction]
        for _ in range(step):
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        direction = (direction + 1) % 4

    return False
```