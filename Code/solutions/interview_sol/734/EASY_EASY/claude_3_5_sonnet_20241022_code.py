```python
def solve(cases):
    results = []
    for n, arr in cases:
        # No solution exists if only 1 color and more than 1 marker
        if len(set(arr)) == 1 and n > 1:
            results.append(["No"])
            continue
            
        # No solution exists if only 1 marker
        if n == 1:
            results.append(["No"])
            continue
            
        # Count frequencies of each color
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
            
        # Not possible if any color appears more than n/2 times
        if any(f > n//2 + (n%2) for f in freq.values()):
            results.append(["No"])
            continue
            
        # Create rotated solution - shift each group of same colors
        colors = list(freq.keys())
        ans = []
        pos = 0
        
        # Place colors rotated one position
        for c in colors:
            count = freq[c]
            next_c = colors[(colors.index(c) + 1) % len(colors)]
            ans.extend([next_c] * count)
            
        # Fix any remaining conflicts by swapping
        for i in range(n):
            if ans[i] == arr[i]:
                for j in range(i+1, n):
                    if ans[j] != arr[i] and ans[i] != arr[j]:
                        ans[i], ans[j] = ans[j], ans[i]
                        break
                        
        results.append(["Yes", ans])
        
    return results
```