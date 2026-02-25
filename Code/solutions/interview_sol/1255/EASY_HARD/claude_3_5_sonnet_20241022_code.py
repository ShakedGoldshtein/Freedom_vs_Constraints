```python
def solve(s, k):
    n = len(s)
    s = set(s)
    
    # Special case - if k=0 and length=26, impossible to create unique string with no common chars
    if k == 0 and n == 26:
        return "NOPE"
        
    # Try building lexicographically smallest valid string
    result = []
    chars_used = set()
    curr_common = 0
    
    for i in range(n):
        # Try each character from a-z
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c in chars_used:
                continue
                
            # Count if adding this char increases common chars
            new_common = curr_common + (1 if c in s else 0)
            
            # If this char keeps us within k common chars
            if new_common <= k:
                result.append(c)
                chars_used.add(c)
                curr_common = new_common
                break
        
        # If we couldn't find any valid char to add
        if len(result) <= i:
            return "NOPE"
            
    return ''.join(result)

def solve_all(test_cases):
    results = []
    for s, k in test_cases:
        results.append(solve(s, k))
    return results
```