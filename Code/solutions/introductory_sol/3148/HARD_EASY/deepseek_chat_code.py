```python
def simplify(directions):
    if not directions:
        return ""
    
    moves = {
        '^': (0, 1),
        'v': (0, -1),
        '<': (-1, 0),
        '>': (1, 0)
    }
    
    x, y = 0, 0
    visited = {(0, 0): 0}
    result = []
    
    for i, direction in enumerate(directions):
        dx, dy = moves[direction]
        x += dx
        y += dy
        
        if (x, y) in visited:
            start_index = visited[(x, y)] + 1
            result = result[:start_index]
            visited = {pos: idx for idx, pos in enumerate(visited) if idx < start_index}
        
        result.append(direction)
        visited[(x, y)] = len(result) - 1
    
    return ''.join(result)
```