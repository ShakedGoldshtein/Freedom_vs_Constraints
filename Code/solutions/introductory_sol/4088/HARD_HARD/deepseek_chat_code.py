```python
def tetris(gamelog):
    field_width = 9
    max_height = 30
    field = [[' ' for _ in range(field_width)] for _ in range(max_height)]
    
    blocks = {
        '1': [(0, 0)],
        '2': [(0, 0), (1, 0)],
        '3': [(0, 0), (1, 0), (2, 0)],
        '4': [(0, 0), (1, 0), (2, 0), (3, 0)]
    }
    
    total_lines_cleared = 0
    
    for command in gamelog:
        if len(command) < 3:
            continue
            
        block_type = command[0]
        direction = command[1]
        offset = int(command[2])
        
        if block_type not in blocks:
            continue
            
        block_cells = blocks[block_type]
        start_col = 4
        
        if direction == 'L':
            start_col -= offset
        else:
            start_col += offset
            
        if start_col < 0 or start_col >= field_width:
            continue
            
        max_col = start_col + len(block_cells) - 1
        if max_col >= field_width:
            continue
            
        landing_row = 0
        for row in range(max_height):
            can_place = True
            for i, (dr, dc) in enumerate(block_cells):
                check_row = row + dr
                check_col = start_col + dc
                
                if check_row >= max_height:
                    can_place = False
                    break
                    
                if field[check_row][check_col] != ' ':
                    can_place = False
                    break
                    
            if not can_place:
                landing_row = row - 1
                break
            else:
                landing_row = row
                
        if landing_row < 0:
            break
            
        for dr, dc in block_cells:
            place_row = landing_row - dr
            place_col = start_col + dc
            if 0 <= place_row < max_height and 0 <= place_col < field_width:
                field[place_row][place_col] = '■'
                
        lines_to_clear = []
        for row in range(max_height):
            if all(cell != ' ' for cell in field[row]):
                lines_to_clear.append(row)
                
        if lines_to_clear:
            lines_to_clear.sort(reverse=True)
            for row in lines_to_clear:
                for r in range(row, 0, -1):
                    field[r] = field[r-1][:]
                field[0] = [' ' for _ in range(field_width)]
                
            total_lines_cleared += len(lines_to_clear)
            
        top_occupied = any(cell != ' ' for cell in field[0])
        if top_occupied:
            break
            
    return total_lines_cleared
```