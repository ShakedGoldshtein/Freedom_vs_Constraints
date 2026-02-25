```python
from collections import deque

def solve(n, q, a, queries):
    results = []
    for m in queries:
        dq = deque(a)
        for _ in range(m - 1):
            A = dq.popleft()
            B = dq.popleft()
            if A > B:
                dq.appendleft(A)
                dq.append(B)
            else:
                dq.appendleft(B)
                dq.append(A)
        A = dq.popleft()
        B = dq.popleft()
        results.append((A, B))
    return results
```