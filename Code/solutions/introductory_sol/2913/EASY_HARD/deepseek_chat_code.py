```python
def x(n):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j or i + j == n - 1:
                row.append('■')
            else:
                row.append('□')
        result.append(''.join(row))
    return '\n'.join(result)
```