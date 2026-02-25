```python
from collections import deque

def solve(n: int, q: int, a: list[int], queries: list[int]) -> list[tuple[int, int]]:
    d = deque(a)
    max_val = max(a)
    max_index = a.index(max_val)
    result = []

    for m in queries:
        if m <= n - 1:
            result.append((a[0], a[1]))
        else:
            cycle_length = n - max_index - 1 if max_index < n - 1 else n - 1
            position_in_cycle = (m - (n - 1)) % cycle_length
            if position_in_cycle == 0:
                position_in_cycle = cycle_length
            A = max_val
            B = a[max_index + position_in_cycle]
            result.append((A, B))

    return result
```