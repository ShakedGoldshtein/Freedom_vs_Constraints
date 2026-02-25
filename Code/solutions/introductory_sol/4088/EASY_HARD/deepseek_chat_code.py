```python
def tetris(gamelog):
    width = 9
    max_height = 30
    field = [[' ' for _ in range(width)] for _ in range(max_height)]
    height = 0
    
    blocks = {
        '1': [(0, 0)],
        '2': [(0, 0), (1, 0)],
        '3': [(0, 0), (1, 0), (2, 0)],
        '4': [(0, 0), (1, 0), (2, 0), (3, 0)]
    }
    
    lines_cleared = 0
    
    for command in gamelog:
        block_type = command[0]
        direction = command[1]
        offset = int(command[2])
        
        start_col = 4
        if direction == 'L':
            start_col -= offset
        else:
            start_col += offset
        
        block_cells = blocks[block_type]
        block_height = len(block_cells)
        
        landing_row = 0
        for row in range(max_height):
            valid = True
            for dr, dc in block_cells:
                check_row = row + dr
                check_col = start_col + dc
                if check_row >= max_height or field[check_row][check_col] != ' ':
                    valid = False
                    break
            if not valid:
                landing_row = row - 1
                break
            landing_row = row
        
        if landing_row < 0:
            break
            
        for dr, dc in block_cells:
            field[landing_row + dr][start_col + dc] = '#'
        
        current_height = landing_row + block_height
        if current_height > height:
            height = current_height
        
        full_lines = []
        for row in range(height):
            if all(cell != ' ' for cell in field[row]):
                full_lines.append(row)
        
        if full_lines:
            lines_cleared += len(full_lines)
            for row in sorted(full_lines, reverse=True):
                del field[row]
                field.insert(0, [' ' for _ in range(width)])
            height -= len(full_lines)
        
        if height >= max_height:
            break
    
    return lines_cleared
```