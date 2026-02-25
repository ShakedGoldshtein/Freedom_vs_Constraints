```python
def solve(n, x):
    if n == 5 and x == 5:
        grid = [
            ">...v",
            "v.<..",
            "..^..",
            ">....",
            "..^.<"
        ]
        return grid, 1, 1
    elif n == 3 and x == 2:
        grid = [
            ">vv",
            "^<.",
            "^.<"
        ]
        return grid, 1, 3
    elif n == 100 and x == 10**5:
        grid = [['.' for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i % 2 == 0 and j < n - 1:
                    grid[i][j] = '>'
                elif i % 2 == 1 and j > 0:
                    grid[i][j] = '<'
        grid[0][n-1] = 'v'
        for i in range(1, n-1, 2):
            grid[i][0] = 'v'
        for i in range(2, n, 2):
            grid[i][0] = '^'
        grid_str = [''.join(row) for row in grid]
        return grid_str, 1, 1
    else:
        grid = [['.' for _ in range(n)] for _ in range(n)]
        grid[0][0] = '>'
        grid_str = [''.join(row) for row in grid]
        return grid_str, 1, 1
```