```python
def solve(n, a):
    result = []
    for i in range(1, n):
        x = 1
        y = 0
        sequence = [i] + a
        visited = set()
        steps = 0
        max_steps = 2 * n
        while True:
            if x <= 0 or x > n:
                result.append(y)
                break
            if (x, y) in visited:
                result.append(-1)
                break
            if steps > max_steps:
                result.append(-1)
                break
            visited.add((x, y))
            steps += 1
            # Step 2: x += a_x, y += a_x
            x_new = x + sequence[x-1]
            y_new = y + sequence[x-1]
            x, y = x_new, y_new
            if x <= 0 or x > n:
                result.append(y)
                break
            # Step 3: y += a_x, x -= a_x
            y_new = y + sequence[x-1]
            x_new = x - sequence[x-1]
            x, y = x_new, y_new
    return result
```