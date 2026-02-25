```python
def solve(n, m, b, g):
    # Check if any boy's minimum is greater than all girls' maximums
    for i in range(n):
        if b[i] > max(g):
            return -1
            
    # Check if any girl's maximum is less than all boys' minimums
    min_b = min(b)
    for j in range(m):
        if g[j] < min_b:
            return -1

    # For each boy, assign their minimum to all girls except one
    # who gets the maximum needed for that girl
    result = 0
    for i in range(n):
        # Add minimum * (m-1) sweets for all but one girl
        result += b[i] * (m-1)
        # Add max needed to satisfy one girl's maximum requirement
        result += max(min(max(g), b[i]+1), b[i])
        
    return result
```