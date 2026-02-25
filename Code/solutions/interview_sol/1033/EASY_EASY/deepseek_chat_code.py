```python
def solve(total_nodes, leaf_values):
    if total_nodes == 1:
        return 0
    
    leaves = leaf_values
    n = total_nodes
    leaf_count = (n + 1) // 2
    
    current_leaves = leaves[:leaf_count]
    
    operations = 0
    nodes = [0] * n
    for i in range(leaf_count):
        nodes[n - leaf_count + i] = current_leaves[i]
    
    for i in range(n - leaf_count - 1, -1, -1):
        left = 2 * i + 1
        right = 2 * i + 2
        if right < n:
            nodes[i] = nodes[left] + nodes[right]
    
    target = max(nodes[0] // leaf_count, 1)
    
    for i in range(leaf_count):
        operations += abs(nodes[n - leaf_count + i] - target)
    
    return operations
```