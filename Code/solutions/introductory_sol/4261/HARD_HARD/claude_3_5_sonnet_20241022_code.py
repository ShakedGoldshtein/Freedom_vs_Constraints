```python
def solve(a):
    def get_next_position(x, y, direction, steps):
        if direction == 0:  # North
            return x, y + steps
        elif direction == 1:  # East
            return x + steps, y  
        elif direction == 2:  # South
            return x, y - steps
        else:  # West
            return x - steps, y

    x, y = 0, 0  # Starting position
    direction = 0  # 0=N, 1=E, 2=S, 3=W
    visited = set([(0,0)])  # Track visited positions
    
    for steps in a:
        # Get next position after moving
        next_x, next_y = get_next_position(x, y, direction, steps)
        
        # Check if we've visited this position before
        if (next_x, next_y) in visited:
            return True
            
        # Add new position to visited set
        visited.add((next_x, next_y))
        
        # Update current position
        x, y = next_x, next_y
        
        # Turn 90 degrees clockwise
        direction = (direction + 1) % 4

    return False
```