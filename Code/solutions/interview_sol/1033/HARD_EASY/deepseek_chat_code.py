```python
def solve(total_nodes, leaf_values):
    if total_nodes == 1:
        return 0
    
    leaf_count = (total_nodes + 1) // 2
    if len(leaf_values) != leaf_count:
        raise ValueError("Number of leaf values does not match the tree structure")
    
    def calculate_min_change(values):
        if len(values) == 1:
            return 0
        
        next_level = []
        for i in range(0, len(values), 2):
            if i + 1 < len(values):
                next_level.append(values[i] + values[i + 1])
            else:
                next_level.append(values[i])
        
        return calculate_min_change(next_level) + sum(abs(values[i] - values[i + 1]) for i in range(0, len(values) - 1, 2))
    
    return calculate_min_change(leaf_values)
```