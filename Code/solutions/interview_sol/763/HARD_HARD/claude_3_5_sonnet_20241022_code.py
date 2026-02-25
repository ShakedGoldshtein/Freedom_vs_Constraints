```python
def is_convertible(s, p):
    """
    Check if binary string s can be converted to p by swapping 1s with 0s
    Time: O(n)
    Space: O(1)
    """
    # If strings already equal, return True
    if s == p:
        return True
        
    # Count number of 0s and 1s in both strings
    s0 = s.count('0')
    s1 = s.count('1') 
    p0 = p.count('0')
    p1 = p.count('1')
    
    # Must have same count of 0s and 1s
    if s0 != p0 or s1 != p1:
        return False
        
    # Check indices where s and p differ
    n = len(s)
    ones_before_zero = False
    zeros_after_one = False
    
    for i in range(n):
        if s[i] != p[i]:
            if s[i] == '1':
                # Need 0 after a 1
                zeros_after_one = True
            else:
                # Need 1 before a 0  
                ones_before_zero = True
                
            if ones_before_zero and zeros_after_one:
                return True
                
    return False

def solve(test_cases):
    """
    Process multiple test cases and return results
    Time: O(T*N) where T is number of test cases and N is max string length
    Space: O(T) for output array
    """
    results = []
    for n, s, p in test_cases:
        result = "Yes" if is_convertible(s, p) else "No"
        results.append(result)
    return results
```