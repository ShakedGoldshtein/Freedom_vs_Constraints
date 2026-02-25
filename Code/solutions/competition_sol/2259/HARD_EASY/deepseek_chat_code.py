```python
def solve(n, q, arr, queries):
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + (1 if arr[i] <= i + 1 else 0)
    
    positions = []
    for i in range(n):
        if arr[i] <= i + 1:
            pos = i + 1 - arr[i]
            if prefix[i + 1] >= pos:
                positions.append(i)
    
    m = len(positions)
    if m == 0:
        answers = [0] * q
        return answers
    
    min_suffix = [0] * m
    min_suffix[-1] = positions[-1]
    for i in range(m - 2, -1, -1):
        min_suffix[i] = min(positions[i], min_suffix[i + 1])
    
    def count_removable(l, r):
        left_idx = -1
        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2
            if positions[mid] >= l:
                left_idx = mid
                high = mid - 1
            else:
                low = mid + 1
        
        if left_idx == -1:
            return 0
        
        right_idx = -1
        low, high = left_idx, m - 1
        while low <= high:
            mid = (low + high) // 2
            if min_suffix[mid] <= r:
                right_idx = mid
                low = mid + 1
            else:
                high = mid - 1
        
        if right_idx == -1:
            return 0
        
        return right_idx - left_idx + 1
    
    answers = []
    for x, y in queries:
        l = x
        r = n - y - 1
        if l > r:
            answers.append(0)
        else:
            answers.append(count_removable(l, r))
    
    return answers
```