```python
def tetris(gamelog):
    FIELD_WIDTH = 9
    FIELD_HEIGHT = 30
    
    # Initialize the game field with empty cells (0)
    # field[y][x], where y=0 is the bottom row, y=29 is the top row.
    field = [[0] * FIELD_WIDTH for _ in range(FIELD_HEIGHT)]
    
    total_cleared_lines = 0

    # Define block shapes as lists of (dy, dx) offsets relative to their bottom-left cell.
    # From the problem description's graphical representation and example trace,
    # these are interpreted as vertical line blocks.
    # dy is the vertical offset from the bottom-most segment, dx is horizontal (always 0 for these shapes).
    BLOCK_SHAPES = {
        1: [(0, 0)],
        2: [(0, 0), (1, 0)],
        3: [(0, 0), (1, 0), (2, 0)],
        4: [(0, 0), (1, 0), (2, 0), (3, 0)]
    }
    # Height of each block type
    BLOCK_HEIGHTS = {
        1: 1, 2: 2, 3: 3, 4: 4
    }

    # Iterate through each command in the gamelog
    for command in gamelog:
        block_type = int(command[0])
        direction = command[1]
        offset = int(command[2])

        block_shape_cells_relative = BLOCK_SHAPES[block_type]
        block_height = BLOCK_HEIGHTS[block_type]

        # Calculate the x-coordinate for the leftmost (and only) column of the block.
        # The center column (L0/R0) is at index 4.
        # 'L' means move left (subtract offset), 'R' means move right (add offset).
        initial_block_x = 4 + (offset if direction == 'R' else -offset)

        # Determine the initial y-coordinate for the bottom of the block when it spawns.
        # Blocks spawn with their highest part at FIELD_HEIGHT - 1 (row 29).
        # So, the bottom of a block of height 'H' would be at (FIELD_HEIGHT - 1) - (H - 1) = FIELD_HEIGHT - H.
        current_bottom_y = FIELD_HEIGHT - block_height

        game_over = False
        # CRITICAL: Check for Game Over condition at spawn location.
        # If any part of the block's initial spawning area is already occupied, the game ends.
        for dy, dx in block_shape_cells_relative:
            target_y = current_bottom_y + dy
            target_x = initial_block_x + dx
            
            # Basic bounds check for x-coordinate (though problem constraints imply valid).
            # The `initial_block_x` ranges from 0 (L4) to 8 (R4), all within FIELD_WIDTH.
            # Since all blocks are 1 unit wide (dx=0), `target_x` will always be valid.
            if not (0 <= target_x < FIELD_WIDTH):
                game_over = True # Should not be hit with valid input
                break
            
            # Check if the spawning cell is already occupied
            if field[target_y][target_x] == 1:
                game_over = True
                break
        
        if game_over:
            break # Game ends immediately if spawn location is blocked

        # Simulate block falling
        # `current_bottom_y` tracks the lowest row the block currently occupies.
        # It falls until it hits the bottom of the field or another block.
        final_bottom_y = current_bottom_y # Default: lands at spawn if cannot fall at all.
        
        while True:
            can_fall_to_next_row = True
            
            # Check if the block can move one step down to `current_bottom_y - 1`.
            for dy, dx in block_shape_cells_relative:
                target_x = initial_block_x + dx
                next_y_for_this_cell = current_bottom_y - 1 + dy # The y-coordinate for this segment in the row below
                
                # Check if this segment would fall below the field boundary (row -1)
                if next_y_for_this_cell < 0:
                    can_fall_to_next_row = False
                    break
                
                # Check for collision with an already placed block in the cell below
                if field[next_y_for_this_cell][target_x] == 1:
                    can_fall_to_next_row = False
                    break
            
            if not can_fall_to_next_row:
                # The block has landed, its bottom is at `current_bottom_y`
                final_bottom_y = current_bottom_y
                break
            
            # If it can fall, move it down one step
            current_bottom_y -= 1

        # Place the block onto the field at its final landed position
        for dy, dx in block_shape_cells_relative:
            field[final_bottom_y + dy][initial_block_x + dx] = 1

        # Check for cleared lines after placing the block
        cleared_rows_indices = []
        for r_idx in range(FIELD_HEIGHT):
            # A row is considered cleared if all its cells are 1 (filled)
            if all(field[r_idx][c_idx] == 1 for c_idx in range(FIELD_WIDTH)):
                cleared_rows_indices.append(r_idx)
        
        if cleared_rows_indices:
            total_cleared_lines += len(cleared_rows_indices)
            
            # Create a new field excluding the cleared rows
            new_field = []
            for r_idx in range(FIELD_HEIGHT):
                if r_idx not in cleared_rows_indices:
                    new_field.append(field[r_idx])
            
            # Add new empty rows to the top of the field to maintain FIELD_HEIGHT
            num_new_rows_needed = len(cleared_rows_indices)
            for _ in range(num_new_rows_needed):
                new_field.append([0] * FIELD_WIDTH)
            
            # Update the game field to the new state
            field = new_field

    return total_cleared_lines
```