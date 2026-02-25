```python
def play_OX_3D(moves):
    board = [[[' ' for _ in range(4)] for _ in range(4)] for _ in range(4)]
    
    def check_winner():
        directions = [
            [(1,0,0), (2,0,0), (3,0,0)], [(0,1,0), (0,2,0), (0,3,0)], [(0,0,1), (0,0,2), (0,0,3)],
            [(1,1,0), (2,2,0), (3,3,0)], [(1,-1,0), (2,-2,0), (3,-3,0)],
            [(1,0,1), (2,0,2), (3,0,3)], [(0,1,1), (0,2,2), (0,3,3)], [(1,1,1), (2,2,2), (3,3,3)],
            [(1,-1,1), (2,-2,2), (3,-3,3)], [(1,1,-1), (2,2,-2), (3,3,-3)], [(1,-1,-1), (2,-2,-2), (3,-3,-3)],
            [(0,0,1), (0,0,2), (0,0,3)], [(0,1,0), (0,2,0), (0,3,0)], [(1,0,0), (2,0,0), (3,0,0)]
        ]
        
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    if board[x][y][z] != ' ':
                        player = board[x][y][z]
                        for dx_list in directions:
                            win = True
                            for dx, dy, dz in dx_list:
                                nx, ny, nz = x + dx, y + dy, z + dz
                                if 0 <= nx < 4 and 0 <= ny < 4 and 0 <= nz < 4:
                                    if board[nx][ny][nz] != player:
                                        win = False
                                        break
                                else:
                                    win = False
                                    break
                            if win:
                                return player
        return None
    
    for i, (x, y, z) in enumerate(moves):
        player = 'O' if i % 2 == 0 else 'X'
        board[x][y][z] = player
        winner = check_winner()
        if winner:
            return f"{winner} wins after {i + 1} moves"
    
    return "No winner"
```