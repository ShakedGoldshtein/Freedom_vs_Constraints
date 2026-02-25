```python
def solve(n, a):
    a.insert(0, 0)
    INF = float('inf')
    result = [-1] * (n + 1)
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        j, s, path = i, 0, []
        while True:
            path.append(j)
            visited[j] = i
            s += a[j]
            if j % 2:
                j += a[j]
            else:
                j -= a[j]
            if j <= 0 or j > n:
                for p in path:
                    result[p] = s
                break
            if visited[j] == i:
                cycle_sum = a[j]
                cycle_len = 1
                k = path.index(j)
                for p in range(k - 1, -1, -1):
                    if path[p] == j:
                        break
                    cycle_sum += a[path[p]]
                    cycle_len += 1
                remaining = (INF - s) % cycle_sum
                for p in range(k - 1, -1, -1):
                    s += a[path[p]]
                    remaining -= a[path[p]]
                    if remaining < 0:
                        result[path[p]] = s + remaining
                    else:
                        result[path[p]] = s
                break
    return result[1:-1]
```