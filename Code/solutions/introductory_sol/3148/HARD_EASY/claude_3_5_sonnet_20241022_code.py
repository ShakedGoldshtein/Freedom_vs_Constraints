```python
def simplify(directions):
    if not directions:
        return ""
        
    # Convert string to list of single steps
    steps = [c for c in directions if c in "^v<>"]
    
    # Track visited coordinates
    x, y = 0, 0
    visited = {(0,0): 0} # coord -> step index when first visited
    path = [(0,0)]
    
    # Map directions to coordinate deltas
    deltas = {
        "^": (0,1),
        "v": (0,-1), 
        "<": (-1,0),
        ">": (1,0)
    }
    
    # Walk through steps and track coordinates
    for i, step in enumerate(steps):
        dx, dy = deltas[step]
        x, y = x + dx, y + dy
        coord = (x,y)
        
        # If coordinate was visited before, we found a loop
        if coord in visited:
            # Remove the loop steps
            loop_start = visited[coord]
            del steps[loop_start:i+1]
            
            # Reset position and continue from before loop
            x, y = path[loop_start][0], path[loop_start][1]
        else:
            visited[coord] = i
            path.append(coord)
            
    return "".join(steps)
```