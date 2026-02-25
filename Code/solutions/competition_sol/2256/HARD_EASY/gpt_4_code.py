```python
def solve(n, m):
    res = []
    x1, y1 = 1, 1
    x2, y2 = n, m

    while x1 <= x2 and y1 <= y2:
        if x1 == x2:
            for y in range(y1, y2 + 1):
                res.append((x1, y))
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                res.append((x, y1))
        else:
            for y in range(y1, y2 + 1):
                res.append((x1, y))
                if y != y2 or x1 == x2:
                    res.append((x2, y2 + 1 - y))

            for x in range(x1 + 1, x2):
                res.append((x, y2))
                res.append((x + 1, y1))

            for y in range(y2 - 1, y1 - 1, -1):
                res.append((x2 + 1 - x1, y))
                if y != y1 or x1 == x2:
                    res.append((x2, y1 + y2 - y))

        x1 += 1
        y1 += 1
        x2 -= 1
        y2 -= 1

    return res
```
