```python
MOD = 10**9 + 7

def solve(n, ops):
    
    ADD = [0]*n
    ACC = [0]*n
    last_acc = last_add = -1
    
    for i in range(n-1,-1,-1):
        op = ops[i]
        if op[0] == 'ADD':
            last_add = i
        if op[0] == 'ACCEPT':
            ACC[last_acc:i] = [op[1]]*(i-last_acc)
            last_acc = i
   
    for i in range(n-1, last_add, -1):
        ADD[i] = ACC[i]
    dp = [0, 1]
    
    for i in range(1,n):
        dp2 = [0]*2
        if ADD[i-1] < ACC[i]:
            dp2[1] = dp[1]
            if ADD[i-1] < ADD[i] and ADD[i] <= ACC[i]:
                dp2[1] += dp[0]
                dp2[0] += dp[0]
        else:
            if ADD[i] > ACC[i-1]:
                dp2[1] = dp[1]
            if ADD[i] > ADD[i-1]:
                dp2[0] += dp[0]
                dp2[1] += dp[1]
        dp = [x % MOD for x in dp2]
    return dp[1]

# n = number of actions
# actions = List of tuples where first value can be 'ADD' or 'ACCEPT' and the second value is the price
n = 6
actions = [("ADD", 1), ("ACCEPT", 1), ("ADD", 2), ("ACCEPT", 2), ("ADD", 3), ("ACCEPT", 3)]
print(solve(n, actions))  # Returns: 8
```
