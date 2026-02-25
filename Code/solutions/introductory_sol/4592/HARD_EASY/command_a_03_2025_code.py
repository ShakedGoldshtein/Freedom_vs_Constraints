```python
def play_3d_tic_tac_toe(moves: list[list[int]]) -> str:
    """
    Determines the winner of a 3D Tic-Tac-Toe game on a 4x4x4 matrix.

    Args:
        moves (list of list of int): A list of moves where each move is [x, y, z] (zero-based).

    Returns:
        str: The result of the game in the format "O wins after X moves", "X wins after X moves", or "No winner".
    """

    # Initialize the 3D board as a 4x4x4 matrix filled with empty strings
    board = [[[" " for _ in range(4)] for _ in range(4)] for _ in range(4)]

    def check_winner() -> str:
        """
        Checks if there is a winner by examining all possible winning lines.

        Returns:
            str: "O" if O wins, "X" if X wins, otherwise empty string.
        """
        # Check all possible lines in 3D space
        lines = []

        # Check rows, columns, and depth in each layer
        for z in range(4):
            for x in range(4):
                line = [board[z][x][y] for y in range(4)]
                lines.append(line)
            for y in range(4):
                line = [board[z][x][y] for x in range(4)]
                lines.append(line)
            for x in range(4):
                line = [board[x][y][z] for y in range(4)]
                lines.append(line)

        # Check vertical lines (depth)
        for x in range(4):
            for y in range(4):
                line = [board[z][x][y] for z in range(4)]
                lines.append(line)

        # Check diagonal planes (4 main diagonals in each layer)
        for z in range(4):
            line1 = [board[z][i][i] for i in range(4)]
            line2 = [board[z][i][3 - i] for i in range(4)]
            lines.append(line1)
            lines.append(line2)

        # Check diagonal depth lines (4 main diagonals through depth)
        for x in range(4):
            line1 = [board[i][x][i] for i in range(4)]
            line2 = [board[i][x][3 - i] for i in range(4)]
            lines.append(line1)
            lines.append(line2)
        for y in range(4):
            line1 = [board[i][i][y] for i in range(4)]
            line2 = [board[i][3 - i][y] for i in range(4)]
            lines.append(line1)
            lines.append(line2)

        # Check 4D diagonals (all 4 diagonals through the cube)
        line1 = [board[i][i][i] for i in range(4)]
        line2 = [board[i][i][3 - i] for i in range(4)]
        line3 = [board[i][3 - i][i] for i in range(4)]
        line4 = [board[i][3 - i][3 - i] for i in range(4)]
        lines.append(line1)
        lines.append(line2)
        lines.append(line3)
        lines.append(line4)

        # Check each line for a win
        for line in lines:
            if line == ["O"] * 4:
                return "O"
            if line == ["X"] * 4:
                return "X"
        return ""

    player = "O"
    move_count = 0

    for move in moves:
        x, y, z = move
        if board[z][x][y] != " ":
            continue  # Skip invalid moves (already occupied)
        board[z][x][y] = player
        move_count += 1
        winner = check_winner()
        if winner:
            return f"{winner} wins after {move_count} moves"
        player = "X" if player == "O" else "O"  # Switch players

    return "No winner"
```