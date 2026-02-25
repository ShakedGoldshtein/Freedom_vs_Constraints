```python
def solve(n, m):
    if n == 1 and m == 1:
        return [(1, 1)]

    total = n * m
    if total == 1:
        return [(1, 1)]

    path = []
    if n == 1:
        for y in range(1, m + 1):
            path.append((1, y))
        return path
    if m == 1:
        for x in range(1, n + 1):
            path.append((x, 1))
        return path

    if n % 2 == 1 and m % 2 == 1:
        return -1

    if n % 2 == 0:
        for x in range(1, n + 1):
            if x % 2 == 1:
                for y in range(1, m + 1):
                    path.append((x, y))
            else:
                for y in range(m, 0, -1):
                    path.append((x, y))
    else:
        for y in range(1, m + 1):
            if y % 2 == 1:
                for x in range(1, n + 1):
                    path.append((x, y))
            else:
                for x in range(n, 0, -1):
                    path.append((x, y))

    return path
```