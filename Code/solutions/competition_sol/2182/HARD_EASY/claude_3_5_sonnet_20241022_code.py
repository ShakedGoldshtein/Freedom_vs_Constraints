```python
def solve(s, t):
    n = len(s)
    
    # Sort each player's letters 
    s_list = sorted(list(s))
    t_list = sorted(list(t), reverse=True)
    
    # Store current state of the game
    result = ['?'] * n
    s_idx = 0  # Index into s_list
    t_idx = 0  # Index into t_list
    
    # Process positions in pairs (one move each from Oleg and Igor)
    for i in range(0, n-1, 2):
        # Find best position for Oleg's letter
        min_idx = -1
        for j in range(n):
            if result[j] == '?':
                min_idx = j
                break
                
        # Find second best position for Igor's letter
        second_idx = -1
        for j in range(min_idx+1, n):
            if result[j] == '?':
                second_idx = j
                break
        
        # Oleg places smallest letter in earliest position
        result[min_idx] = s_list[s_idx]
        s_idx += 1
        
        # Igor places largest letter in second position
        if second_idx != -1:
            result[second_idx] = t_list[t_idx]
            t_idx += 1
            
    # Handle last position if n is odd
    if n % 2 == 1:
        for i in range(n):
            if result[i] == '?':
                result[i] = s_list[s_idx]
                break
                
    return ''.join(result)
```