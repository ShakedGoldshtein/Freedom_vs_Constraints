```python
def determine_3d_tic_tac_toe_winner(moves):
    """
    Determines the winner of a 3D Tic-Tac-Toe game on a 4x4x4 board.

    Args:
        moves: List of tuples [x, y, z] representing the sequence of moves (0-based).

    Returns:
        str: "O wins after {move_count} moves", "X wins after {move_count} moves", or "No winner".
    """
    board = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]
    directions = _get_directions()

    for move_idx, (x, y, z) in enumerate(moves, 1):
        if not (0 <= x < 4 and 0 <= y < 4 and 0 <= z < 4):
            continue  # Skip invalid moves (though problem says input is valid)
        if board[x][y][z] is not None:
            continue  # Skip if cell already occupied (though problem says moves are valid)

        player = 'O' if move_idx % 2 == 1 else 'X'
        board[x][y][z] = player

        if _check_win(board, x, y, z, player, directions):
            return f"{player} wins after {move_idx} moves"

    return "No winner"

def _get_directions():
    """Returns all 26 possible winning directions in 3D (4-length lines)."""
    directions = []
    # Axial lines (parallel to x, y, or z axis)
    for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        directions.extend([
            (dx, dy, dz),
            (-dx, -dy, -dz)
        ])
    # Diagonal lines within a single plane (2D diagonals in any plane)
    for plane in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]:
        a, b, c = plane
        for da, db in [(1, 1), (1, -1)]:
            dirs = [(0, 0, 0)] * 3
            dirs[a], dirs[b] = da, db
            directions.extend([tuple(dirs), tuple(-d for d in dirs)])
    # Space diagonals (3D diagonals)
    for dx, dy, dz in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]:
        directions.extend([(dx, dy, dz), (-dx, -dy, -dz)])
    return directions

def _check_win(board, x, y, z, player, directions):
    """Checks if the last move at (x,y,z) results in a win for the player."""
    for dx, dy, dz in directions:
        count = 1  # The current cell is already occupied by the player
        # Check in the positive direction
        for step in range(1, 4):
            nx, ny, nz = x + dx * step, y + dy * step, z + dz * step
            if not (0 <= nx < 4 and 0 <= ny < 4 and 0 <= nz < 4):
                break
            if board[nx][ny][nz] != player:
                break
            count += 1
        # Check in the negative direction
        for step in range(1, 4):
            nx, ny, nz = x - dx * step, y - dy * step, z - dz * step
            if not (0 <= nx < 4 and 0 <= ny < 4 and 0 <= nz < 4):
                break
            if board[nx][ny][nz] != player:
                break
            count += 1
        if count >= 4:
            return True
    return False
```