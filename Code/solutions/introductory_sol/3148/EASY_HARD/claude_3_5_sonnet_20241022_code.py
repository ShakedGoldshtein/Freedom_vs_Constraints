```python
def simplify(directions):
    if not directions:
        return ""
        
    # Track visited coordinates
    visited = set([(0,0)])
    path = [(0,0)]
    current = [0,0]
    result = []
    
    # Map directions to coordinate changes
    dir_map = {
        "^": (0,1),
        "v": (0,-1),
        "<": (-1,0), 
        ">": (1,0)
    }
    
    for d in directions:
        if d not in dir_map:
            continue
            
        dx, dy = dir_map[d]
        current[0] += dx
        current[1] += dy
        coord = tuple(current)
        
        if coord in visited:
            # Found a loop - backtrack to remove it
            while path[-1] != coord:
                visited.remove(path.pop())
                result.pop()
        else:
            visited.add(coord)
            path.append(coord)
            result.append(d)
            
    return "".join(result)
```