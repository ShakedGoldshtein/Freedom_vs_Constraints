```python
def play_3d_tic_tac_toe(moves):
    """
    Play 3D Tic-Tac-Toe on a 4x4x4 grid and determine the winner.
    
    Args:
        moves: List of [x,y,z] coordinates (zero-based)
    
    Returns:
        String indicating winner or "No winner"
    """
    if not moves:
        return "No winner"
    
    # Initialize 3D board (4x4x4)
    board = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]
    
    # All possible winning directions in 3D
    directions = []
    
    # Generate all possible lines of 4 in 3D space
    for i in range(4):
        for j in range(4):
            # Rows in x-direction (fixed y,z)
            directions.append([(x, j, i) for x in range(4)])
            # Rows in y-direction (fixed x,z)
            directions.append([(i, y, j) for y in range(4)])
            # Rows in z-direction (fixed x,y)
            directions.append([(i, j, z) for z in range(4)])
            
            # Diagonals in xy-plane (fixed z)
            if i == j:
                directions.append([(k, k, i) for k in range(4)])
            if i + j == 3:
                directions.append([(k, 3-k, i) for k in range(4)])
            
            # Diagonals in xz-plane (fixed y)
            if i == j:
                directions.append([(k, i, k) for k in range(4)])
            if i + j == 3:
                directions.append([(k, i, 3-k) for k in range(4)])
            
            # Diagonals in yz-plane (fixed x)
            if i == j:
                directions.append([(i, k, k) for k in range(4)])
            if i + j == 3:
                directions.append([(i, k, 3-k) for k in range(4)])
    
    # 3D diagonals
    directions.append([(i, i, i) for i in range(4)])
    directions.append([(i, i, 3-i) for i in range(4)])
    directions.append([(i, 3-i, i) for i in range(4)])
    directions.append([(3-i, i, i) for i in range(4)])
    
    # Remove duplicates
    unique_directions = []
    for direction in directions:
        if direction not in unique_directions:
            unique_directions.append(direction)
    
    # Play the game
    for move_num, (x, y, z) in enumerate(moves):
        # Validate move coordinates
        if not (0 <= x < 4 and 0 <= y < 4 and 0 <= z < 4):
            continue
            
        # Check if position is already occupied
        if board[x][y][z] is not None:
            continue
            
        # Make the move (O goes first, then alternates)
        player = 'O' if move_num % 2 == 0 else 'X'
        board[x][y][z] = player
        
        # Check for winner
        for direction in unique_directions:
            line = [board[dx][dy][dz] for dx, dy, dz in direction]
            if all(cell == player for cell in line):
                return f"{player} wins after {move_num + 1} moves"
    
    return "No winner"
```