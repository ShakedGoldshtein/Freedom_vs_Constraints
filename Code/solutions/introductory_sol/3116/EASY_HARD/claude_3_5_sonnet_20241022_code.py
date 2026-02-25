```python
def cal_n_bug(heads, legs, pairs_wings):
    # Define matrix A for the system of linear equations
    A = [[1, 1, 1],      # heads equation
         [8, 6, 6],      # legs equation
         [0, 1, 2]]      # wings equation
    
    # Try all possible integer combinations within reasonable bounds
    for s in range(heads + 1):
        for b in range(heads + 1):
            d = heads - s - b
            
            if d < 0:
                continue
                
            # Check if this combination satisfies all equations
            if (8*s + 6*b + 6*d == legs and
                b + 2*d == pairs_wings):
                return [s, b, d]
    
    return [-1, -1, -1]
```