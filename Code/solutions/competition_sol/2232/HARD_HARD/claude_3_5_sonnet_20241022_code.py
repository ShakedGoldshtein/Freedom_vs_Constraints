```python
def solve(n):
    # Returns list of number of + presses needed at each level
    result = []
    
    # Start at 2 at level 1
    curr_num = 2
    curr_level = 1
    
    while curr_level <= n:
        # For each level, determine number of plus presses needed
        # to reach next perfect square divisible by next level
        plus_presses = 0
        target_found = False
        
        # Try each number of plus presses until we find one that works
        while not target_found:
            # After these many plus presses
            test_num = curr_num + plus_presses * curr_level
            
            # Check if it's a perfect square
            sqrt = int(test_num ** 0.5)
            if sqrt * sqrt == test_num:
                # The sqrt needs to be divisible by next level
                if sqrt % (curr_level + 1) == 0:
                    target_found = True
                    curr_num = sqrt
                    result.append(plus_presses)
                    curr_level += 1
            
            if not target_found:
                plus_presses += 1
                
            # Make sure we don't get too large numbers
            if plus_presses > 10**18:
                # Reset and try a different approach
                plus_presses = 0
                curr_num += curr_level
    
    return result

```