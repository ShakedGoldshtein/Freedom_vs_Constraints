```python
def simplify(directions):
    moves = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
    x, y = 0, 0
    visited = {(0, 0): 0}
    result = []
    
    for i, d in enumerate(directions):
        dx, dy = moves[d]
        x += dx
        y += dy
        
        if (x, y) in visited:
            j = visited[(x, y)]
            result = result[:j]
            visited = {pos: idx for idx, pos in enumerate([(0, 0)] + [(px, py) for px, py, _ in result])}
            x, y = result[-1][0], result[-1][1] if result else (0, 0)
        else:
            result.append((x, y, d))
            visited[(x, y)] = len(result)
    
    return ''.join(d for _, _, d in result)
```