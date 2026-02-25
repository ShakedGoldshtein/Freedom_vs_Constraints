```python
def solve(n, A, k):
    if n <= k:
        return sum(A)
        
    # dp[i][j][p] represents max money when using i keys on left side
    # and j keys on right side having used p keys in total
    dp = {}
    
    def helper(left, right, keys_used):
        if keys_used == k:
            return 0
        
        if (left, right, keys_used) in dp:
            return dp[(left, right, keys_used)]
            
        # Can only unlock rooms adjacent to already unlocked rooms
        
        # Try unlocking from left
        left_money = 0
        if left < n and (left == 0 or left-1 <= keys_used - right):
            left_money = A[left] + helper(left+1, right, keys_used+1)
            
        # Try unlocking from right    
        right_money = 0
        if right >= 0 and (right == n-1 or n-right-2 <= keys_used - left):
            right_money = A[right] + helper(left, right-1, keys_used+1)
            
        dp[(left, right, keys_used)] = max(left_money, right_money)
        return dp[(left, right, keys_used)]
    
    return helper(0, n-1, 0)
```