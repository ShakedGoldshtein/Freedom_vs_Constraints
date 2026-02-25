```python
def solve(moves):
    def check_line(a, b, c, d):
        return a == b == c == d and a != ' '
    
    def check_winner(board):
        # Check all rows in each layer
        for z in range(4):
            for y in range(4):
                if check_line(board[z][y][0], board[z][y][1], board[z][y][2], board[z][y][3]):
                    return board[z][y][0]
                    
        # Check all columns in each layer
        for z in range(4):
            for x in range(4):
                if check_line(board[z][0][x], board[z][1][x], board[z][2][x], board[z][3][x]):
                    return board[z][0][x]
                    
        # Check all depth lines
        for y in range(4):
            for x in range(4):
                if check_line(board[0][y][x], board[1][y][x], board[2][y][x], board[3][y][x]):
                    return board[0][y][x]
                    
        # Check diagonals in each layer
        for z in range(4):
            if check_line(board[z][0][0], board[z][1][1], board[z][2][2], board[z][3][3]):
                return board[z][0][0]
            if check_line(board[z][0][3], board[z][1][2], board[z][2][1], board[z][3][0]):
                return board[z][0][3]
                
        # Check diagonal planes parallel to x
        for x in range(4):
            if check_line(board[0][0][x], board[1][1][x], board[2][2][x], board[3][3][x]):
                return board[0][0][x]
            if check_line(board[0][3][x], board[1][2][x], board[2][1][x], board[3][0][x]):
                return board[0][3][x]
                
        # Check diagonal planes parallel to y
        for y in range(4):
            if check_line(board[0][y][0], board[1][y][1], board[2][y][2], board[3][y][3]):
                return board[0][y][0]
            if check_line(board[0][y][3], board[1][y][2], board[2][y][1], board[3][y][0]):
                return board[0][y][3]
                
        # Check main diagonals
        if check_line(board[0][0][0], board[1][1][1], board[2][2][2], board[3][3][3]):
            return board[0][0][0]
        if check_line(board[0][0][3], board[1][1][2], board[2][2][1], board[3][3][0]):
            return board[0][0][3]
        if check_line(board[0][3][0], board[1][2][1], board[2][1][2], board[3][0][3]):
            return board[0][3][0]
        if check_line(board[0][3][3], board[1][2][2], board[2][1][1], board[3][0][0]):
            return board[0][3][3]
            
        return None

    # Initialize empty board
    board = [[[ ' ' for x in range(4)] for y in range(4)] for z in range(4)]
    
    # Play moves
    for i, move in enumerate(moves):
        player = 'O' if i % 2 == 0 else 'X'
        z, y, x = move
        
        # Place piece
        if board[z][y][x] == ' ':
            board[z][y][x] = player
        
        # Check for winner
        winner = check_winner(boar