```python
def solve(t, test_cases):
    # Segments needed for each digit
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    
    def get_max_num(n):
        # Can't display anything with less than 2 segments
        if n < 2:
            return 0
            
        # Find max number of digits possible with n segments
        digits = []
        remaining = n
        
        # Greedily select digits that give most value for segments used
        while remaining >= 2:  # 2 is min segments needed
            # Try to use 1 (2 segments) where possible as it gives best value
            if remaining >= 2:
                digits.append(1)
                remaining -= 2
                
        # Handle remaining segments by trying to improve rightmost digits
        for i in range(len(digits)-1, -1, -1):
            # Try each digit from 9 down to current
            curr_segments = 2 # segments for digit 1
            for d in range(9, digits[i]-1, -1):
                if remaining + curr_segments >= segments[d]:
                    remaining = remaining + curr_segments - segments[d]
                    digits[i] = d
                    break
                    
        # Convert digits array to number
        if not digits:
            return 0
            
        result = 0
        for d in digits:
            result = result * 10 + d
            
        return result

    # Process each test case    
    results = []
    for n in test_cases:
        results.append(get_max_num(n))
        
    return results
```