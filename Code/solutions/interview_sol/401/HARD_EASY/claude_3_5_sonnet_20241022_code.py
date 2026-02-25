```python
def maxSumDivThree(nums):
    """
    Find maximum sum divisible by 3 from array elements
    
    Args:
        nums: List[int] - Input array of integers
        
    Returns:
        int - Maximum possible sum divisible by 3
    """
    # dp[i] represents max sum when remainder with 3 is i
    dp = [0, 0, 0]
    
    for num in nums:
        # Create temporary copy of current state
        temp = dp.copy()
        
        for remainder in range(3):
            # For each remainder state, try adding current number
            curr_sum = temp[remainder] + num
            # Update dp array with max possible sum for new remainder state
            dp[curr_sum % 3] = max(dp[curr_sum % 3], curr_sum)
    
    # Return maximum sum divisible by 3
    return dp[0]
```