```python
def solve(moves):
    def check_win(board, player):
        # check rows, cols in each layer
        for z in range(4):
            for i in range(4):
                if all(board[i][j][z] == player for j in range(4)) or \
                   all(board[j][i][z] == player for j in range(4)):
                    return True
                    
        # check vertical lines            
        for x in range(4):
            for y in range(4):
                if all(board[x][y][z] == player for z in range(4)):
                    return True
        
        # check diagonals in each layer
        for z in range(4):
            if all(board[i][i][z] == player for i in range(4)) or \
               all(board[i][3-i][z] == player for i in range(4)):
                return True
        
        # check 3D diagonals
        if all(board[i][i][i] == player for i in range(4)) or \
           all(board[i][i][3-i] == player for i in range(4)) or \
           all(board[i][3-i][i] == player for i in range(4)) or \
           all(board[3-i][i][i] == player for i in range(4)):
            return True
            
        # check diagonal planes
        for i in range(4):
            if all(board[i][j][j] == player for j in range(4)) or \
               all(board[i][j][3-j] == player for j in range(4)) or \
               all(board[j][i][j] == player for j in range(4)) or \
               all(board[j][i][3-j] == player for j in range(4)) or \
               all(board[j][j][i] == player for j in range(4)) or \
               all(board[j][3-j][i] == player for j in range(4)):
                return True
                
        return False

    # initialize empty board
    board = [[['' for z in range(4)] for y in range(4)] for x in range(4)]
    
    for i, (x, y, z) in enumerate(moves):
        player = 'O' if i % 2 == 0 else 'X'
        board[x][y][z] = player
        
        if check_win(board, player):
            return f"{player} wins after {i+1} moves"
            
    return "No winner"
```