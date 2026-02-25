```python
def solve(n: int, m: int, b: list, g: list) -> int:
    """
    Find minimum total sweets given min sweets per boy and max sweets per girl.
    
    Args:
        n: Number of boys
        m: Number of girls 
        b: List of minimum sweets per boy
        g: List of maximum sweets per girl
        
    Returns:
        Minimum total sweets possible, or -1 if impossible
    """
    # Check if max per girl >= min per any boy
    for i in range(n):
        if min(g) < b[i]:
            return -1
            
    # For each boy, we need to give at least b[i] sweets to each girl
    # except one girl who gets exactly b[i]
    min_total = 0
    
    # For each boy i:
    for i in range(n):
        min_total += b[i] * m  # Minimum b[i] to all m girls
        
    # For each girl j, we need at least one boy to give her g[j]
    # Let's greedily assign the max values where needed
    g_sorted = sorted(enumerate(g), key=lambda x: -x[1]) # Sort by decreasing g[j]
    b_sorted = sorted(enumerate(b), key=lambda x: -x[1]) # Sort by decreasing b[i]
    
    girl_covered = [False] * m
    boy_used = [False] * n
    assigned = 0
    
    # Try to assign each girl her max value
    for j, g_val in g_sorted:
        found = False
        # Look for an unused boy with b[i] <= g[j]
        for i, b_val in b_sorted:
            if not boy_used[i] and b_val <= g_val:
                boy_used[i] = True
                girl_covered[j] = True
                assigned += 1
                min_total += g_val - b[i] # Add difference needed
                found = True
                break
        if not found:
            return -1
                
    return min_total
```