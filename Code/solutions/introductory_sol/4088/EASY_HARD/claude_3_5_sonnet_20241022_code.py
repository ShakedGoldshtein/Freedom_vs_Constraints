```python
def tetris(gamelog):
    field = [[0] * 9 for _ in range(30)]
    blocks = {
        1: [(0,0)],
        2: [(0,0), (1,0)],
        3: [(0,0), (1,0), (2,0)], 
        4: [(0,0), (1,0), (2,0), (3,0)]
    }
    
    def can_place(x, y, block_type):
        for dx, dy in blocks[block_type]:
            ny = y + dy
            nx = x + dx
            if ny >= 30 or nx < 0 or nx >= 9:
                return False
            if ny < 0:
                continue
            if field[ny][nx]:
                return False
        return True
    
    def place_block(x, y, block_type):
        for dx, dy in blocks[block_type]:
            ny = y + dy
            nx = x + dx
            if ny >= 0:
                field[ny][nx] = 1
                
    def check_lines():
        lines = 0
        y = 29
        while y >= 0:
            if all(field[y]):
                lines += 1
                for row in range(y, 0, -1):
                    field[row] = field[row-1][:]
                field[0] = [0] * 9
            else:
                y -= 1
        return lines
    
    cleared = 0
    for command in gamelog:
        block = int(command[0])
        direction = command[1]
        offset = int(command[2])
        
        x = 4  # start at center
        if direction == 'L':
            x -= offset
        else:
            x += offset
            
        y = -len(blocks[block])
        
        while y < 30 and can_place(x, y+1, block):
            y += 1
            
        if y >= 30:
            break
            
        place_block(x, y, block)
        cleared += check_lines()
        
    return cleared
```