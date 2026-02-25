```python
from collections import deque

def solve(n, q, arr, queries):
    if q == 0:
        return []
    
    # Find cycle length and state before cycle
    seen = {}
    deq = deque(arr)
    step = 0
    state = tuple(deq)
    
    while state not in seen:
        seen[state] = step
        a = deq.popleft()
        b = deq.popleft()
        if a > b:
            deq.appendleft(a)
            deq.append(b)
        else:
            deq.appendleft(b) 
            deq.append(a)
        step += 1
        state = tuple(deq)
    
    cycle_start = seen[state]
    cycle_len = step - cycle_start
    
    # Process each query
    result = []
    for m in queries:
        m = m - 1  # Convert to 0-based indexing
        
        # Reconstruct deque state for this operation
        if m < cycle_start:
            pos = m
        else:
            pos = ((m - cycle_start) % cycle_len) + cycle_start
            
        deq = deque(arr)
        for _ in range(pos):
            a = deq.popleft()
            b = deq.popleft()
            if a > b:
                deq.appendleft(a)
                deq.append(b)
            else:
                deq.appendleft(b)
                deq.append(a)
                
        result.append([deq[0], deq[1]])
        
    return result
```