```python
import heapq

def minimum_chairs(N, M, LiRi):
    LiRi.sort(reverse=True)
    be_treated, end_at = [], 0
    for i in range(N-1, -1, -1):
        Li, Ri = LiRi[i]
        while be_treated and be_treated[0] <= Li:
            _, p = heapq.heappop(be_treated)
            if p < Li:
                end_at += 1
        heapq.heappush(be_treated, (Ri, Li))
        if len(be_treated) > M + 1 - Li:
            _, p = heapq.heappop(be_treated)
            end_at = max(end_at, p)
    while be_treated:
        _, p = heapq.heappop(be_treated)
        end_at = max(end_at, p)
    return end_at - M + N
```