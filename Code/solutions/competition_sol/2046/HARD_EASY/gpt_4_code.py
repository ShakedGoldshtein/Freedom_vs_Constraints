```python
def solve_cow_program(n, a):
    a = [0] + a
    result = []
    for y in range(1, n):
        x = y
        total = 0
        visited = [0]*len(a)
        while 1 <= x < n:
            if visited[x] == -1:
                total = -1
                break
            elif visited[x] == 1:
                total += a[x]
                x += a[x]
                visited[x] = -1
            else:
                total += a[x]
                x += a[x]
                visited[x - a[x]] = 1
        result.append(total)
    return result
```