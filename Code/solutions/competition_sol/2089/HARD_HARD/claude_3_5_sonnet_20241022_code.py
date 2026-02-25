```python
def solve(n, operations):
    """
    Generate simplified CALPAS program that is functionally equivalent to input program.
    
    Args:
        n: Number of operations in input program
        operations: List of (op, val) tuples where op is '&', '|' or '^' and val is 0-1023
        
    Returns:
        Tuple of (k, simplified_ops) where:
            k: Number of operations in simplified program (0-5)
            simplified_ops: List of (op, val) tuples for simplified program
    """
    def simulate(x, ops):
        """Simulate running program on input x"""
        for op, val in ops:
            if op == '&': x &= val
            elif op == '|': x |= val 
            else: x ^= val
        return x
    
    # Special case - if all XOR, can be combined to single or zero XORs
    if all(op == '^' for op, _ in operations):
        val = 0
        for _, x in operations:
            val ^= x
        if val == 0:
            return 0, []
        return 1, [('^', val)]
            
    # Special case - if all AND, can be combined to single AND
    if all(op == '&' for op, _ in operations):
        val = 1023 # All 1s
        for _, x in operations:
            val &= x
        return 1, [('&', val)]
        
    # Get program results for all possible inputs
    results = {}
    for i in range(1024):
        results[i] = simulate(i, operations)
        
    # Try programs of increasing length until we find one that matches
    for k in range(1, 6):
        for ops in range(3**k): # Try all possible op combinations
            candidate = []
            tmp = ops
            for _ in range(k):
                op = tmp % 3
                tmp //= 3
                if op == 0: candidate.append(('&', 0))
                elif op == 1: candidate.append(('|', 0)) 
                else: candidate.append(('^', 0))
                
            # Try all possible values for each operation
            def try_values(pos, curr_ops):
                if pos == k:
                    # Test if candidate matches for all inputs
                    match = True
                    for x in range(1024):
                        if simulate(x, curr_ops) != results[x]:
                            match = False
                            break
                    if match:
                        return curr_ops
                    return None
                
                # Try values 0-1023 for current operation
                op = curr_ops[pos][0]
                for val in range(1024):
                    curr_ops[pos] = (op, val)
                    res = try_values(pos+1, curr_ops)
                    if res:
                        return res
                return None
            
            res = try_values(0, candidate)
            if res:
                return k, res
                
    return n, operations
```