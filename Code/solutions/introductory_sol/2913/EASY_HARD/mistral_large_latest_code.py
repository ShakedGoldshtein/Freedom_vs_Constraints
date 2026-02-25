```python
def x_shape(n):
    result = []
    for i in range(n):
        line = []
        for j in range(n):
            if i == j or i + j == n - 1:
                line.append('■')
            else:
                line.append('□')
        result.append(''.join(line))
    return '\n'.join(result)
```