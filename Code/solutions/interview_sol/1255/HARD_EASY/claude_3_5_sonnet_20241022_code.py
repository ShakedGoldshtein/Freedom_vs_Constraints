```python
def solve_single_case(s: str, k: int) -> str:
    n = len(s)
    s_set = set(s)
    
    # Special case: if k=0, we need string with no common chars
    if k == 0:
        # Start with smallest possible chars
        result = []
        curr_char = 'a'
        
        # Find first n chars not in s
        while len(result) < n:
            if curr_char not in s_set:
                result.append(curr_char)
            if curr_char == 'z':
                return "NOPE"
            curr_char = chr(ord(curr_char) + 1)
            
        return ''.join(result)

    # If k equals length, can return lexicographically smallest string 
    # of same length with unique chars
    if k == n:
        result = []
        curr_char = 'a'
        while len(result) < n:
            result.append(curr_char)
            curr_char = chr(ord(curr_char) + 1)
        return ''.join(result)

    # For other cases, try to use as few common chars as possible
    # while maintaining lexicographic order
    result = []
    curr_char = 'a' 
    common_used = 0
    
    while len(result) < n:
        if curr_char > 'z':
            return "NOPE"
            
        if curr_char in s_set:
            if common_used < k:
                result.append(curr_char)
                common_used += 1
        else:
            result.append(curr_char)
            
        curr_char = chr(ord(curr_char) + 1)
        
    return ''.join(result)

def solve(t: int, cases: list) -> list:
    results = []
    for s, k in cases:
        results.append(solve_single_case(s, k))
    return results
```