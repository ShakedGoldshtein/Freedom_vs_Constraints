```python
def tetris(gamelog):
    FIELD_WIDTH = 9
    FIELD_HEIGHT = 30
    BLOCKS = {
        1: [(0, 0), (1, 0)],
        2: [(0, 0), (0, 1), (1, 1)],
        3: [(0, 0), (0, 1), (0, 2)],
        4: [(0, 0), (0, 1), (1, 0), (1, 1)]
    }

    field = [bytearray(FIELD_WIDTH) for _ in range(FIELD_HEIGHT)]
    current_height = 0
    cleared_lines = 0

    for command in gamelog:
        if current_height >= FIELD_HEIGHT:
            break

        block_type = int(command[0])
        direction = command[1]
        offset = int(command[2])

        block = BLOCKS[block_type]
        block_width = max(x for x, y in block) + 1
        block_height = max(y for x, y in block) + 1

        start_col = 4 + (offset if direction == 'R' else -offset)
        start_col = max(0, min(start_col, FIELD_WIDTH - block_width))

        if start_col + block_width > FIELD_WIDTH:
            continue

        new_height = current_height + block_height
        if new_height > FIELD_HEIGHT:
            return cleared_lines

        for x, y in block:
            field[current_height + y][start_col + x] = 1

        current_height = new_height

        while True:
            full_line = -1
            for y in range(current_height):
                if all(field[y]):
                    full_line = y
                    break

            if full_line == -1:
                break

            cleared_lines += 1
            for y in range(full_line, current_height - 1):
                field[y] = field[y + 1][:]
            current_height -= 1
            field[current_height] = bytearray(FIELD_WIDTH)

    return cleared_lines
```