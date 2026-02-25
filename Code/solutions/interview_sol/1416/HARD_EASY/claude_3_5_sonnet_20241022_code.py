```python
def solve(n, values):
    """
    Divides stones between Han Solo and Chewbacca optimally.
    
    Args:
        n: Number of stones
        values: List of stone values in order
        
    Returns:
        Tuple of (han_stones, chewie_stones) where each is a list of values
    """
    # Calculate target sizes for each half
    size1 = n // 2 if n % 2 == 0 else (n + 1) // 2
    size2 = n - size1
    
    # Initialize DP array: dp[i][j][k] represents minimum difference possible using i stones,
    # with j stones in first group and k stones in second group
    dp = {}
    
    def divide_stones(pos, count1, count2, sum1, sum2, used1, used2):
        if (pos, count1, count2) in dp:
            return dp[(pos, count1, count2)]
            
        # Base case - reached end of stones
        if pos >= n:
            if count1 == size1 and count2 == size2:
                return abs(sum1 - sum2), used1, used2
            return float('inf'), [], []
            
        # Cannot exceed target sizes
        if count1 > size1 or count2 > size2:
            return float('inf'), [], []
            
        # Try putting stone in first group
        diff1 = float('inf')
        res1_used1, res1_used2 = [], []
        if count1 < size1:
            diff1, u1, u2 = divide_stones(pos + 1, count1 + 1, count2, 
                                        sum1 + values[pos], sum2,
                                        used1 + [values[pos]], used2)
            res1_used1, res1_used2 = u1, u2
            
        # Try putting stone in second group    
        diff2 = float('inf')
        res2_used1, res2_used2 = [], []
        if count2 < size2:
            diff2, u1, u2 = divide_stones(pos + 1, count1, count2 + 1,
                                        sum1, sum2 + values[pos],
                                        used1, used2 + [values[pos]])
            res2_used1, res2_used2 = u1, u2
            
        # Pick better option
        if diff1 < diff2:
            dp[(pos, count1, count2)] = (diff1, res1_used1, res1_used2)
        else:
            dp[(pos, count1, count2)] = (diff2, res2_used1, res2_used2)
            
        return dp[(pos, count1, count2)]
        
    # First stone must go to Han Solo
    _, han_stones, chewie_stones = divide_stones(1, 1, 0, values[0], 0, [values[0]], [])
    
    return han_stones, chewie_stones
```