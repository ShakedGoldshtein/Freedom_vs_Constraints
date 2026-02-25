```python
def solve(t, test_cases):
    segments = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    min_segments = 2  # minimum segments needed for any digit (digit 1)
    
    def max_number(n):
        if n < min_segments:
            return -1
        
        # Try to use as many 1's as possible (2 segments each)
        length = n // 2
        remaining = n % 2
        
        if remaining == 1:
            length -= 1
            remaining += 2
            
        # Form number with max 1's and potentially one bigger digit
        result = ['1'] * length
        
        if remaining:
            # Find largest digit that can be shown with remaining segments
            for d in range(9, -1, -1):
                if segments[d] == remaining:
                    result.append(str(d))
                    break
                    
        if not result:
            return 0
        result.sort(reverse=True)
        return int(''.join(result))
    
    result = []
    for n in test_cases:
        result.append(max_number(n))
    return result
```