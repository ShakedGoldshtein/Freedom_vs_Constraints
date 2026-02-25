```python
def solve(a):
    # Track current position and direction
    x, y = 0, 0
    dx, dy = 0, 1  # Initially facing north (0,1)
    
    # Track visited points
    visited = {(0,0)}
    
    for steps in a:
        # Take steps forward
        x2 = x + dx * steps
        y2 = y + dy * steps
        
        # Add all points along path to visited set
        if dx == 0:  # Moving vertically
            step = 1 if y2 > y else -1
            for py in range(y, y2 + step, step):
                if (x, py) in visited:
                    return True
                visited.add((x, py))
        else:  # Moving horizontally 
            step = 1 if x2 > x else -1
            for px in range(x, x2 + step, step):
                if (px, y) in visited:
                    return True
                visited.add((px, y))
                
        # Update position
        x, y = x2, y2
        
        # Turn 90 degrees clockwise by rotating direction vector
        dx, dy = dy, -dx
        
    return False
```