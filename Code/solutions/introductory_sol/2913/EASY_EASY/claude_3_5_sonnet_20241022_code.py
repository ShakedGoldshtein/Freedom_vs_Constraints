```python
def x_shape(n):
    lines = []
    for i in range(n):
        line = ['□'] * n
        line[i] = '■'
        line[n-1-i] = '■'
        lines.append(''.join(line))
    return '\n'.join(lines)
```