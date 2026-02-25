```python
def solve(n, leaf_values):
    # For single node, no change needed
    if n == 1:
        return 0
        
    # Get number of leaf nodes from total nodes n
    num_leaf_nodes = (n + 1) // 2
    
    # If input leaf values don't match expected number of leaf nodes, return -1
    if len(leaf_values) != num_leaf_nodes:
        return -1
    
    def get_min_cost(target_val, leaf_values):
        total_change = 0
        for val in leaf_values:
            total_change += abs(target_val - val)
        return total_change
    
    # Binary search on optimal target value
    left = min(leaf_values)
    right = max(leaf_values)
    
    while right - left > 2:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        cost1 = get_min_cost(mid1, leaf_values)
        cost2 = get_min_cost(mid2, leaf_values) 
        
        if cost1 < cost2:
            right = mid2
        else:
            left = mid1
            
    # Find minimum cost in the range
    min_cost = float('inf')
    for target in range(left, right + 1):
        cost = get_min_cost(target, leaf_values)
        min_cost = min(min_cost, cost)
        
    # Calculate if any change needed to total sum
    original_sum = sum(leaf_values)
    target_leaf_val = (left + right) // 2
    target_sum = target_leaf_val * len(leaf_values)
    
    return abs(target_sum - original_sum)
```