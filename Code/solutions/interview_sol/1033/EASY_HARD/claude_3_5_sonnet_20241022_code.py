```python
def solve(n, leaf_values):
    if n == 1:
        return 0
        
    if n == 3:
        # For 2 leaf nodes case
        return 0
    
    # Get number of leaf nodes from total nodes
    leaf_nodes = (n + 1) // 2
    
    # Target value is the average of all leaf nodes
    target = sum(leaf_values[:leaf_nodes]) / leaf_nodes
    target = int(target)
    
    # Calculate minimum difference needed
    total_change = 0
    for i in range(leaf_nodes):
        total_change += abs(leaf_values[i] - target)
    
    # Return minimum of making all leaves equal to floor or ceil of average    
    return int(total_change // 2)
```