```python
from heapq import *
def solve(T, data):
    result = []
    for idx in range(T):
        N, K, E, M, *data = data
        scores = [-sum(data[i:i+E]) for i in range(0, (N-1)*E, E)]
        sergey = sum(data[(N-1)*E:-1])
        heapify(scores)
        for _ in range(K-1):
            heappop(scores)
        min_points = -scores[0]-sergey+1
        if min_points > M:
            result.append("Impossible")
        else:
            result.append(max(0, min_points))
    return result
```