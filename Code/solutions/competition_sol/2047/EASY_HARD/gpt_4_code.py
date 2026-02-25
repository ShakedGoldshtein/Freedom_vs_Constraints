```python
def parking(n, k, grid):
    moves = []
    r, c = None, None
    for j in range(n):
        if grid[1][j] > 0 and grid[0][j] == grid[1][j]:
            moves.append((grid[1][j], 0, j))
            grid[1][j] = 0
            k -= 1
        if grid[2][j] > 0 and grid[3][j] == grid[2][j]:
            moves.append((grid[2][j], 3, j))
            grid[2][j] = 0
            k -= 1
        if grid[1][j] == 0 or grid[2][j] == 0:
            r, c = 2, j
    if r is None:
        if grid[1][0] == 0:
            r, c = 1, 0
        else:
            r, c = 2, 0
    while k > 0:
        cr, cc = r, c
        if r == 2:
            if c == 0:
                r += 1
            else:
                c -= 1
        else:
            if c == n - 1:
                r -= 1
            else:
                c += 1
        if grid[cr][cc] > 0:
            if r == 0 and grid[r][c] == grid[cr][cc]:
                moves.append((grid[cr][cc], r, c))
                grid[cr][cc] = 0
                k -= 1
            elif r == 3 and grid[r][c] == grid[cr][cc]:
                moves.append((grid[cr][cc], r, c))
                grid[cr][cc] = 0
                k -= 1
            else:
                if r == 0:
                    r += 1
                else:
                    r -= 1
        else:
            if grid[cr][cc] > 0:
                moves.append((grid[cr][cc], r, c))
                grid[r][c] = grid[cr][cc]
                grid[cr][cc] = 0
    if len(moves) > 20000:
        return -1
    else:
        return len(moves), moves
```