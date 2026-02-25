```python
def solve(n, values):
    total_sum = sum(values)
    target_sum = total_sum // 2
    
    if n % 2 == 0:
        k = n // 2
    else:
        k = (n - 1) // 2
    
    dp = [[False] * (target_sum + 1) for _ in range(k + 1)]
    dp[0][0] = True
    path = [[None] * (target_sum + 1) for _ in range(k + 1)]
    
    for idx, val in enumerate(values):
        for count in range(min(k, idx + 1), 0, -1):
            for s in range(target_sum, val - 1, -1):
                if dp[count - 1][s - val] and not dp[count][s]:
                    dp[count][s] = True
                    path[count][s] = idx
    
    best_sum = 0
    for s in range(target_sum, -1, -1):
        if dp[k][s]:
            best_sum = s
            break
    
    han_set = []
    chewie_set = []
    used = [False] * n
    
    current_count = k
    current_sum = best_sum
    while current_count > 0 and current_sum > 0:
        for idx in range(n - 1, -1, -1):
            if path[current_count][current_sum] == idx:
                han_set.append(values[idx])
                used[idx] = True
                current_count -= 1
                current_sum -= values[idx]
                break
    
    for i in range(n):
        if not used[i]:
            chewie_set.append(values[i])
    
    han_set.reverse()
    
    han_first = []
    chewie_first = []
    
    for val in values:
        if val in han_set and (not han_first or val == han_set[len(han_first)]):
            han_first.append(val)
            han_set.remove(val)
        else:
            chewie_first.append(val)
            if val in chewie_set:
                chewie_set.remove(val)
    
    han_output = ' '.join(map(str, han_first))
    chewie_output = ' '.join(map(str, chewie_first))
    
    return han_output, chewie_output
```