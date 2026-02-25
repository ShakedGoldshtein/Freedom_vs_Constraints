```python
def solve(n, arr):
    used = [False] * n
    sequences = []
    
    while any(not x for x in used):
        curr_seq = []
        prev = float('-inf')
        
        for i in range(n):
            if used[i]:
                continue
                
            if not curr_seq or arr[i] > prev:
                curr_seq.append(arr[i])
                prev = arr[i]
                used[i] = True
        
        sequences.append(curr_seq)
        
    # Convert sequences to string representation
    result = []
    for seq in sequences:
        result.append(' '.join(map(str, seq)))
    return result
```