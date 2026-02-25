```python
def solve(N, M, intervals):
    events = []
    for l, r in intervals:
        events.append((l, 1))
        events.append((r + 1, -1))
    
    events.sort()
    
    active = 0
    max_active = 0
    i = 0
    for pos in range(1, M + 2):
        while i < len(events) and events[i][0] == pos:
            active += events[i][1]
            i += 1
        max_active = max(max_active, active)
    
    return max(0, max_active - M)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    intervals = []
    idx = 2
    for _ in range(N):
        L = int(data[idx])
        R = int(data[idx + 1])
        intervals.append((L, R))
        idx += 2
    
    result = solve(N, M, intervals)
    print(result)

if __name__ == "__main__":
    main()
```