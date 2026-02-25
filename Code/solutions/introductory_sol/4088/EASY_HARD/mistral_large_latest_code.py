```python
def tetris(gamelog):
    field = [[0 for _ in range(9)] for _ in range(30)]
    blocks = [
        [[1, 0]],  # Block 1: single square
        [[1, 0], [0, 1], [1, 1]],  # Block 2: L-shape
        [[1, 0], [1, 1], [0, 1]],  # Block 3: mirrored L-shape
        [[1, 0], [1, 1], [1, 2], [1, 3]]  # Block 4: I-shape
    ]
    current_height = 0
    cleared_lines = 0

    for cmd in gamelog:
        if current_height >= 30:
            break
        block_type = int(cmd[0]) - 1
        direction = cmd[1]
        offset = int(cmd[2])

        # Calculate starting position (center is index 4)
        start_col = 4
        if direction == 'L':
            start_col -= offset
        else:  # R
            start_col += offset

        # Get block pattern and adjust for current height
        block = blocks[block_type]
        block_rows = max(y for y, x in block) + 1
        block_cols = max(x for y, x in block) + 1

        # Check if block fits horizontally
        min_x = min(x for y, x in block)
        max_x = max(x for y, x in block)
        if start_col + min_x < 0 or start_col + max_x >= 9:
            continue  # Block doesn't fit, skip command

        # Place the block
        for y, x in block:
            row = current_height + y
            col = start_col + x
            if row >= 30:
                return cleared_lines
            field[row][col] = 1

        # Update current height
        current_height += block_rows

        # Check for completed lines and clear them
        lines_to_clear = []
        for row in range(current_height):
            if all(field[row]):
                lines_to_clear.append(row)

        if lines_to_clear:
            # Count cleared lines
            cleared_lines += len(lines_to_clear)
            # Remove cleared lines and shift down
            for row in sorted(lines_to_clear, reverse=True):
                del field[row]
                field.insert(0, [0 for _ in range(9)])
            current_height -= len(lines_to_clear)

    return cleared_lines
```