```python
def solve(N, M, intervals):
    events = []
    for l, r in intervals:
        events.append((l, 1))
        events.append((r + 1, -1))
    
    events.sort()
    
    count = 0
    active = 0
    last_pos = 0
    for pos, typ in events:
        if pos > last_pos:
            count = max(count, active - (pos - last_pos - 1))
            active = max(0, active - (pos - last_pos))
        active += typ
        last_pos = pos
    
    return max(0, N - M - count)
```