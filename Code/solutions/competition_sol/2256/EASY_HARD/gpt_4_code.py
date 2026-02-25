```python
def solve(n, m):
    result = []
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                result.append((i+1, j+1))
            else:
                result.append((i+1, m-j))
    if n % 2 != 0:
        result = result[:m] + result[m:][::-1]
    return result
```