```python
def tetris(gamelog):
    def create_field():
        return [[0 for _ in range(9)] for _ in range(30)]

    def get_block_coords(block_type, start_x):
        if block_type == 1:
            return [(0, start_x)]
        elif block_type == 2:
            return [(0, start_x), (1, start_x)]
        elif block_type == 3:
            return [(0, start_x), (1, start_x), (2, start_x)]
        else:  # block_type == 4
            return [(0, start_x), (1, start_x), (2, start_x), (3, start_x)]

    def can_place_block(field, coords):
        for y, x in coords:
            if y >= 30 or x < 0 or x >= 9 or field[y][x]:
                return False
        return True

    def place_block(field, coords):
        for y, x in coords:
            field[y][x] = 1

    def move_block_down(field, coords):
        new_coords = [(y + 1, x) for y, x in coords]
        if can_place_block(field, new_coords):
            return new_coords
        return None

    def clear_lines(field):
        lines_cleared = 0
        y = 29
        while y >= 0:
            if all(field[y]):
                lines_cleared += 1
                for row in range(y, 0, -1):
                    field[row] = field[row - 1][:]
                field[0] = [0] * 9
            else:
                y -= 1
        return lines_cleared

    def calculate_start_x(direction, offset):
        center = 4
        if direction == 'L':
            return center - offset
        return center + offset

    field = create_field()
    total_lines_cleared = 0

    for command in gamelog:
        block_type = int(command[0])
        direction = command[1]
        offset = int(command[2])
        
        start_x = calculate_start_x(direction, offset)
        coords = get_block_coords(block_type, start_x)
        
        if not can_place_block(field, coords):
            break
            
        while True:
            new_coords = move_block_down(field, coords)
            if not new_coords:
                break
            coords = new_coords
            
        place_block(field, coords)
        if coords[0][0] == 0:
            break
            
        total_lines_cleared += clear_lines(field)

    return total_lines_cleared
```