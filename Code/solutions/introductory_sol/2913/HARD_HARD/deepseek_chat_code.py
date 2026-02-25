```python
def x(n):
    if n < 3 or n % 2 == 0:
        raise ValueError("n must be an odd integer >= 3")
    
    grid = [['□' for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        grid[i][i] = '■'
        grid[i][n - 1 - i] = '■'
    
    return '\n'.join(''.join(row) for row in grid)
```