Here is the Python code to solve the problem.

```python
import heapq

def solve(N, M, LR):
    LR.sort(key=lambda x: (x[1], -x[0]))
    L, ans, heap = [], 0, []
    for x, y in LR:
        if len(L) < M: heapq.heappush(L, x)
        elif L and L[0] < x:
            heapq.heappush(L, x)
            heapq.heappop(L)
    while L: heap.append(heapq.heappop(L))
    heap.sort()
    for x, y in LR:
        if heap and heap[0] < x:
            heapq.heappop(heap)
            ans += 1
    return ans
```

This piece of code visually represents a line where chairs are sequentially placed. It uses `heap` data structure to take care of the situation of possibly adding chairs. Given the list of constraints for each person (left and right indices), it chooses the best possible place for the person to sit. The sort methods ensure that person gets to sit in the place they prefer most. If there is no place within the person's preferred indices, then a chair is added, and the count is incremented. Ultimately, the minimum number of additional chairs required is returned.