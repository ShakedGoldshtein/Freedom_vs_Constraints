```python
def count_good_substrings(s):
    n = len(s)
    result = 0
    
    # For each starting position
    for l in range(n):
        # Try different lengths 
        for length in range(1, min(20, n-l+1)):
            # Get substring from l to r
            r = l + length - 1
            if r >= n:
                break
                
            # Get substring and convert to decimal
            substr = s[l:r+1]
            decimal = int(substr, 2)
            
            # Check if length equals decimal value
            if length == decimal:
                result += 1
                
    return result

def solve(t, strings):
    result = []
    for s in strings:
        result.append(count_good_substrings(s))
    return result
```