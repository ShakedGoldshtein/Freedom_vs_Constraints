```python
def solve(s, t):
    freq_s = {}
    freq_t = {}
    
    # Count frequencies in s
    for c in s:
        freq_s[c] = freq_s.get(c, 0) + 1
        
    # Count frequencies in t
    for c in t:
        freq_t[c] = freq_t.get(c, 0) + 1
    
    steps = 0
    # For each char in t, check if we need to replace it
    for c in freq_t:
        if c in freq_s:
            # If char exists in s but with lower freq, we need to replace extra occurrences
            if freq_t[c] > freq_s[c]:
                steps += freq_t[c] - freq_s[c]
        else:
            # If char doesn't exist in s, we need to replace all occurrences
            steps += freq_t[c]
            
    return steps
```