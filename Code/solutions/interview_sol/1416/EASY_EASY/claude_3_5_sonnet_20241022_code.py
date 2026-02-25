```python
def solve(n, values):
    # Initialize dp table and solution tracking
    dp = {}
    path = {}
    total = sum(values)
    
    # Get target sizes for each half based on odd/even n
    size1 = n//2 if n % 2 == 0 else (n+1)//2
    size2 = n//2 if n % 2 == 0 else (n-1)//2
    
    def find_subset(pos, count1, sum1, selected):
        if count1 > size1:
            return float('inf')
        if pos == n:
            if count1 == size1:
                return abs((total - sum1) - sum1)
            return float('inf')
            
        state = (pos, count1, sum1, selected)
        if state in dp:
            return dp[state]
        
        # Try including current element in first set
        include = find_subset(pos+1, count1+1, sum1+values[pos], selected | (1 << pos))
        
        # Try excluding current element
        exclude = find_subset(pos+1, count1, sum1, selected)
        
        if include < exclude:
            dp[state] = include
            path[state] = True
        else:
            dp[state] = exclude 
            path[state] = False
            
        return dp[state]
    
    # Find optimal split
    min_diff = find_subset(0, 0, 0, 0)
    
    # Reconstruct solution
    han_solo = []
    chewbacca = []
    
    state = (0, 0, 0, 0)
    pos = 0
    count1 = 0
    sum1 = 0
    selected = 0
    
    while pos < n:
        state = (pos, count1, sum1, selected)
        if path.get(state, False):
            han_solo.append(values[pos])
            count1 += 1
            sum1 += values[pos]
            selected |= (1 << pos)
        else:
            chewbacca.append(values[pos])
        pos += 1
        
    return han_solo, chewbacca
```