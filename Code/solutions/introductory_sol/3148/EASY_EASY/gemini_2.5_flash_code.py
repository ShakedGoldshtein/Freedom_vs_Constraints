```python
def simplify(directions: str) -> str:
    current_x, current_y = 0, 0
    
    # Stores the simplified path characters (directions)
    simplified_path_chars = []
    
    # Stores the coordinates corresponding to each point in the simplified path.
    # simplified_path_positions[0] is the starting point (0,0).
    # For i > 0, simplified_path_positions[i] is the coordinate reached after taking the (i-1)-th direction
    # in simplified_path_chars.
    simplified_path_positions = [(0, 0)]
    
    # Maps (x, y) coordinates to the index in `simplified_path_positions` where that coordinate was last visited
    # in the *current* simplified path.
    visited_coords = {(0, 0): 0}
    
    # Movement deltas for each direction character
    dx = {'<': -1, '>': 1, '^': 0, 'v': 0}
    dy = {'<': 0, '>': 0, '^': 1, 'v': -1}
    
    for direction_char in directions:
        # Calculate the next potential position
        next_x = current_x + dx[direction_char]
        next_y = current_y + dy[direction_char]
        next_pos = (next_x, next_y)
        
        if next_pos in visited_coords:
            # A loop is detected: John has returned to a previously visited coordinate.
            # `loop_start_idx` is the index in `simplified_path_positions` where `next_pos` was first reached
            # in the current simplified path.
            loop_start_idx = visited_coords[next_pos]
            
            # Truncate the path to remove the loop segment.
            # This means removing all directions and positions that were added *after* `loop_start_idx`.
            simplified_path_chars = simplified_path_chars[:loop_start_idx]
            
            # `simplified_path_positions` stores coordinates, including the start (index 0).
            # So, `simplified_path_positions[loop_start_idx]` is the coordinate where the loop began.
            # We keep this coordinate and all preceding ones.
            simplified_path_positions = simplified_path_positions[:loop_start_idx + 1]
            
            # Update `visited_coords`: remove all entries whose index is greater than `loop_start_idx`.
            # This ensures `visited_coords` accurately reflects only the positions present in the
            # now-truncated `simplified_path_positions`.
            visited_coords = {pos: idx for pos, idx in visited_coords.items() if idx <= loop_start_idx}
            
            # After removing the loop, the current position is now `next_pos`.
            current_x, current_y = next_x, next_y
            
        else:
            # No loop detected, extend the path by adding the current direction and new position.
            simplified_path_chars.append(direction_char)
            simplified_path_positions.append(next_pos)
            
            # Record the new position and its index in `visited_coords`.
            # The index is the last index of `simplified_path_positions`.
            visited_coords[next_pos] = len(simplified_path_positions) - 1
            
            # Update the current coordinates.
            current_x, current_y = next_x, next_y
            
    # Join the simplified path characters to form the final string of directions.
    return "".join(simplified_path_chars)
```