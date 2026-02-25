```python
def solve(N, pairs):
    all_nums = []
    for x, y in pairs:
        all_nums.append(x)
        all_nums.append(y)
    all_nums.sort()
    
    total_len = 2 * N
    candidate1 = (all_nums[N - 1] - all_nums[0]) * (all_nums[total_len - 1] - all_nums[N])
    
    min_r = float('inf')
    max_r = 0
    min_b = float('inf')
    max_b = 0
    
    for i in range(N):
        a, b = pairs[i]
        if a > b:
            a, b = b, a
        min_r = min(min_r, a)
        max_r = max(max_r, a)
        min_b = min(min_b, b)
        max_b = max(max_b, b)
    
    candidate2 = (max_r - min_r) * (max_b - min_b)
    
    pairs.sort(key=lambda p: max(p[0], p[1]))
    
    min_second = float('inf')
    max_second = 0
    min_first = float('inf')
    
    for i in range(N):
        a, b = pairs[i]
        if a > b:
            a, b = b, a
        min_first = min(min_first, a)
        max_second = max(max_second, b)
        if i < N - 1:
            min_second = min(min_second, b)
    
    fixed_max_red = max_second
    fixed_min_red = min_first
    
    for i in range(N):
        a, b = pairs[i]
        if a > b:
            a, b = b, a
        if i == N - 1:
            if N > 1:
                candidate_min_red = min(min_first, pairs[N-2][1] if pairs[N-2][0] > pairs[N-2][1] else pairs[N-2][0])
            else:
                candidate_min_red = min_first
        else:
            candidate_min_red = min_first
        
        candidate_max_red = fixed_max_red
        if i < N - 1:
            candidate_min_blue = min_second
        else:
            candidate_min_blue = min(b for j, (x, y) in enumerate(pairs) if j != i)
        
        candidate_max_blue = max(b for j, (x, y) in enumerate(pairs) if j != i)
        
        candidate3 = (candidate_max_red - candidate_min_red) * (candidate_max_blue - candidate_min_blue)
        candidate2 = min(candidate2, candidate3)
    
    return min(candidate1, candidate2)
```