```python
def solve(N, pairs):
    numbers = []
    for x, y in pairs:
        numbers.append(x)
        numbers.append(y)
    numbers.sort()
    
    ans = float('inf')
    n = 2 * N
    
    # Try all possible continuous segments for red balls
    for i in range(N + 1):
        for j in range(i, n - (N - i)):
            possible = True
            red_nums = numbers[i:j + 1]
            blue_nums = numbers[:i] + numbers[j + 1:]
            
            # Check if this partition is valid (one ball per bag)
            ball_count = {}
            for x, y in pairs:
                ball_count[(x, y)] = 0
                if x in red_nums:
                    ball_count[(x, y)] += 1
                if y in red_nums:
                    ball_count[(x, y)] += 1
                    
            for count in ball_count.values():
                if count != 1:
                    possible = False
                    break
                    
            if possible:
                red_diff = red_nums[-1] - red_nums[0]
                blue_diff = blue_nums[-1] - blue_nums[0]
                ans = min(ans, red_diff * blue_diff)
    
    return ans
```