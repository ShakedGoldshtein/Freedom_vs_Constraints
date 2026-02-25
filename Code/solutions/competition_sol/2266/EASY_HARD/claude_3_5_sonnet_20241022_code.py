```python
def solve(n, m, lr_pairs):
    events = []
    for l, r in lr_pairs:
        events.append((l, 1))  # Add 1 for starting point
        events.append((r - 1, -1))  # Subtract 1 for ending point
        
    events.sort()
    
    # Track number of people needing seats at each point
    active_demands = 0
    max_demands = 0
    
    # Track number of chairs available at each point
    chairs = 0
    curr_pos = 0
    
    for pos, change in events:
        if pos != curr_pos and active_demands > chairs:
            max_demands = max(max_demands, active_demands - chairs)
        
        active_demands += change
        
        # If integer position, add a chair
        if pos.is_integer() and 1 <= pos <= m:
            chairs = 1
        else:
            chairs = 0
            
        curr_pos = pos
    
    # Check final position
    if active_demands > chairs:
        max_demands = max(max_demands, active_demands - chairs)
        
    return max_demands
```