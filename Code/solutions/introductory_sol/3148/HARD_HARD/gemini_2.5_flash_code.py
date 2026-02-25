```python
class InvalidDirectionError(ValueError):
    """Custom exception for invalid direction characters."""
    pass

# Define direction changes as (delta_x, delta_y)
# The problem description has a typo: "v" and ">" cannot both be "east".
# Based on common convention and the provided examples, we assume standard
# cardinal directions for the symbols:
# '^': North (y increases)
# 'v': South (y decreases)
# '<': West (x decreases)
# '>': East (x increases)
_DIRECTION_DELTAS = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0),
}

def simplify(directions: str) -> str:
    """
    Simplifies a list of directional movements by eliminating any loops.

    A loop is defined as any sublist of directions which leads John to a
    coordinate he had already visited in the *current* simplified path.
    When a loop is detected, the directions forming that loop (from the
    point of the previous visit to the current point, including the current
    move) are discarded. This effectively "undoes" the path segment that
    led back to an already visited location.

    Args:
        directions: A string of characters representing the path.
                    Valid characters are '^', 'v', '<', '>'.

    Returns:
        A string representing the simplified path with no loops.

    Raises:
        InvalidDirectionError: If the input string contains characters
                               other than '^', 'v', '<', '>'.

    Time Complexity: O(N), where N is the length of the input `directions` string.
                     Each character is processed once. Appends/pops to lists
                     and dictionary operations are amortized O(1). In the worst
                     case, each direction character results in one push and one
                     pop operation across the entire execution.
    Space Complexity: O(N), for storing the `path_coords` (list of coordinates),
                      `path_dirs` (list of direction characters), and
                      `coord_to_idx` (dictionary for quick lookup).
    """
    if not directions:
        return ""

    # (current_x, current_y) represents John's current position on the grid.
    # John starts at (0,0) before taking any steps.
    current_x, current_y = 0, 0

    # `path_coords`: A list of (x, y) tuples representing the coordinates
    # visited in the *simplified* path. This acts as a stack where the most
    # recent position is at the end.
    path_coords = [(current_x, current_y)]

    # `path_dirs`: A list of characters representing the *simplified* directions
    # that lead to the corresponding positions in `path_coords`. This also acts
    # as a stack, synchronized with `path_coords`.
    path_dirs = []

    # `coord_to_idx`: A dictionary mapping (x, y) coordinates to their
    # *index* in `path_coords`. This allows O(1) average time lookup
    # to quickly detect if a coordinate has been visited and where in the
    # `path_coords` stack it was last encountered. This map must always
    # reflect the current state of `path_coords`.
    coord_to_idx = {(current_x, current_y): 0}

    for char_dir in directions:
        delta = _DIRECTION_DELTAS.get(char_dir)
        if delta is None:
            raise InvalidDirectionError(
                f"Invalid direction character: '{char_dir}'. "
                f"Expected one of {list(_DIRECTION_DELTAS.keys())}."
            )
        
        delta_x, delta_y = delta

        next_x = current_x + delta_x
        next_y = current_y + delta_y
        next_pos = (next_x, next_y)

        if next_pos in coord_to_idx:
            # Loop detected: John is moving to a coordinate `next_pos` that
            # has already been visited in the current `path_coords`.
            
            # `loop_start_idx` is the index in `path_coords` where `next_pos`
            # was previously visited. This marks the beginning of the segment
            # that will be removed.
            loop_start_idx = coord_to_idx[next_pos]
            
            # Backtrack: Remove all coordinates and directions from `path_coords`
            # and `path_dirs` that were part of the loop. This means popping
            # elements until the `path_coords` stack length is `loop_start_idx + 1`.
            # `loop_start_idx + 1` ensures `next_pos` (the loop detection point)
            # remains as the last element in `path_coords`.
            while len(path_coords) > loop_start_idx + 1:
                removed_coord = path_coords.pop()
                # When a coordinate is removed from `path_coords`, it must also
                # be removed from `coord_to_idx` to maintain consistency.
                del coord_to_idx[removed_coord]
                path_dirs.pop()
            
            # After backtracking, the `current_pos` effectively becomes `next_pos`
            # (the loop detection point), and the direction that led to this
            # loop is discarded.
            current_x, current_y = next_pos
            
            # The current `char_dir` (which led to `next_pos`) is discarded,
            # and we move to process the next character in the input `directions`.
            continue
        else:
            # No loop detected: `next_pos` is a new, unvisited coordinate
            # (within the context of the current simplified path).
            # Add this new position and the corresponding direction to our
            # simplified path stacks.
            path_coords.append(next_pos)
            path_dirs.append(char_dir)
            
            # Record the index of this new coordinate for future loop detection.
            coord_to_idx[next_pos] = len(path_coords) - 1
            
            # Update John's current position.
            current_x, current_y = next_pos

    # Join the simplified direction characters to form the final result string.
    return "".join(path_dirs)
```