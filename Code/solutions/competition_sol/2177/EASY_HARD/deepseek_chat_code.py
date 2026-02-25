```python
def solve(n, a):
    from collections import deque
    min_val = min(a)
    count = {}
    for num in a:
        count[num] = count.get(num, 0) + 1
    
    positions = {}
    for idx, num in enumerate(a):
        if num not in positions:
            positions[num] = deque()
        positions[num].append(idx)
    
    total_operations = 0
    current_pos = 0
    remaining = n
    
    while remaining > 0:
        if count.get(min_val, 0) > 0:
            pos_queue = positions[min_val]
            while pos_queue and pos_queue[0] < current_pos:
                pos_queue.append(pos_queue.popleft() + n)
            
            if pos_queue:
                next_pos = pos_queue.popleft()
                total_operations += (next_pos - current_pos) % n + 1
                current_pos = (next_pos + 1) % n
                count[min_val] -= 1
                remaining -= 1
            else:
                min_val += 1
        else:
            min_val += 1
    
    return total_operations
```