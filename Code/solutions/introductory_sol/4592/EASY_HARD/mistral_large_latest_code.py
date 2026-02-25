```python
def tic_tac_toe_3d(moves):
    grid = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]
    current_player = 'O'

    for i, (x, y, z) in enumerate(moves, 1):
        grid[x][y][z] = current_player
        if check_win(grid, x, y, z, current_player):
            return f"{current_player} wins after {i} moves"
        current_player = 'X' if current_player == 'O' else 'O'

    return "No winner"

def check_win(grid, x, y, z, player):
    # Check line in x-axis
    if all(grid[x][y][k] == player for k in range(4)):
        return True
    # Check line in y-axis
    if all(grid[x][k][z] == player for k in range(4)):
        return True
    # Check line in z-axis
    if all(grid[k][y][z] == player for k in range(4)):
        return True
    # Check diagonals in xy-plane (fixed z)
    if x == y and all(grid[k][k][z] == player for k in range(4)):
        return True
    if x + y == 3 and all(grid[k][3-k][z] == player for k in range(4)):
        return True
    # Check diagonals in xz-plane (fixed y)
    if x == z and all(grid[k][y][k] == player for k in range(4)):
        return True
    if x + z == 3 and all(grid[k][y][3-k] == player for k in range(4)):
        return True
    # Check diagonals in yz-plane (fixed x)
    if y == z and all(grid[x][k][k] == player for k in range(4)):
        return True
    if y + z == 3 and all(grid[x][k][3-k] == player for k in range(4)):
        return True
    # Check 3D diagonals
    if x == y == z and all(grid[k][k][k] == player for k in range(4)):
        return True
    if x + y + z == 3 and y == 3 - x and all(grid[k][k][3-k] == player for k in range(4)):
        return True
    if x + y + z == 3 and x == 3 - y and all(grid[k][3-k][k] == player for k in range(4)):
        return True
    if x + y + z == 3 and z == 3 - x and all(grid[3-k][k][k] == player for k in range(4)):
        return True
    return False
```