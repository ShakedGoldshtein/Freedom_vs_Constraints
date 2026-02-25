```python
def solve(n, a_list):
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = a_list[i - 2]
    
    dp = [0] * (n + 1)
    res = []
    
    for start in range(2, n + 1):
        if dp[start] != 0:
            res.append(dp[start])
            continue
            
        visited = set()
        path = []
        cur = start
        y = 0
        valid = True
        
        while True:
            if cur <= 0 or cur > n:
                break
            if cur == 1:
                valid = False
                break
            if cur in visited:
                valid = False
                break
            if dp[cur] != 0:
                y += dp[cur]
                break
                
            visited.add(cur)
            path.append(cur)
            y += a[cur]
            cur += a[cur]
            
            if cur <= 0 or cur > n:
                break
                
            y += a[cur]
            cur -= a[cur]
            
        if valid:
            for node in path:
                dp[node] = y
                y -= a[node]
        else:
            for node in path:
                dp[node] = -1
                
        res.append(dp[start])
    
    return res
```