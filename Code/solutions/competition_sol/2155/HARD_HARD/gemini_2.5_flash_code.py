```python
def max_total_gain(n: int, m: int, grid: list[list[int]]) -> int:
    """
    Calculates the maximum total calorie gain for Iahub and Iahubina's workout.

    Iahub starts at (0, 0) and aims for (n-1, m-1), moving only down or right.
    Iahubina starts at (n-1, 0) and aims for (0, m-1), moving only up or right.
    They meet in exactly one cell (r, c), where neither performs a workout.
    Their paths must cross at this meeting cell, meaning Iahub enters (r, c)
    from one adjacent cell and leaves to another, while Iahubina enters (r, c)
    from an adjacent cell and leaves to another, such that their pre-meeting and
    post-meeting path segments do not overlap except at (r, c) itself.

    Args:
        n: The number of rows in the gym grid (1-indexed in problem, 0-indexed in code).
        m: The number of columns in the gym grid (1-indexed in problem, 0-indexed in code).
        grid: A list of lists of integers where grid[i][j] is calories burned
              at cell (i, j).

    Returns:
        The maximum total gain possible, which is the sum of calories from all
        unique cells visited by either Iahub or Iahubina, excluding the meet cell.

    Optimal Time Complexity: O(N*M)
    Optimal Space Complexity: O(N*M)
    """
    # Use a sufficiently small negative number to represent unreachable paths.
    # Since calories are non-negative (0 <= a[i][j]), any valid path sum will be >= 0.
    N_INF = float('-inf')

    # dp_iahub_to_rc[r][c]: Max calories Iahub gains to reach (r, c) from (0, 0).
    # Iahub moves down (r+1, c) or right (r, c+1). Includes grid[r][c].
    dp_iahub_to_rc = [[N_INF] * m for _ in range(n)]

    # dp_iahub_from_rc[r][c]: Max calories Iahub gains to reach (n-1, m-1) from (r, c).
    # This is calculated by a reverse DP, moving up (r-1, c) or left (r, c-1) from (n-1, m-1).
    # Includes grid[r][c].
    dp_iahub_from_rc = [[N_INF] * m for _ in range(n)]

    # dp_iahubina_to_rc[r][c]: Max calories Iahubina gains to reach (r, c) from (n-1, 0).
    # Iahubina moves up (r-1, c) or right (r, c+1). Includes grid[r][c].
    dp_iahubina_to_rc = [[N_INF] * m for _ in range(n)]

    # dp_iahubina_from_rc[r][c]: Max calories Iahubina gains to reach (0, m-1) from (r, c).
    # This is calculated by a reverse DP, moving down (r+1, c) or left (r, c-1) from (0, m-1).
    # Includes grid[r][c].
    dp_iahubina_from_rc = [[N_INF] * m for _ in range(n)]

    # --- Calculate dp_iahub_to_rc (Iahub from (0,0) to (r,c)) ---
    dp_iahub_to_rc[0][0] = grid[0][0]
    for r in range(n):
        for c in range(m):
            if r == 0 and c == 0:
                continue
            val_from_up = dp_iahub_to_rc[r - 1][c] if r > 0 else N_INF
            val_from_left = dp_iahub_to_rc[r][c - 1] if c > 0 else N_INF
            
            if val_from_up != N_INF or val_from_left != N_INF:
                dp_iahub_to_rc[r][c] = grid[r][c] + max(val_from_up, val_from_left)

    # --- Calculate dp_iahub_from_rc (Iahub from (r,c) to (n-1,m-1)) ---
    # This is equivalent to finding the path from (n-1,m-1) to (r,c) moving up/left.
    dp_iahub_from_rc[n - 1][m - 1] = grid[n - 1][m - 1]
    for r in range(n - 1, -1, -1):
        for c in range(m - 1, -1, -1):
            if r == n - 1 and c == m - 1:
                continue
            val_from_down = dp_iahub_from_rc[r + 1][c] if r < n - 1 else N_INF
            val_from_right = dp_iahub_from_rc[r][c + 1] if c < m - 1 else N_INF

            if val_from_down != N_INF or val_from_right != N_INF:
                dp_iahub_from_rc[r][c] = grid[r][c] + max(val_from_down, val_from_right)

    # --- Calculate dp_iahubina_to_rc (Iahubina from (n-1,0) to (r,c)) ---
    dp_iahubina_to_rc[n - 1][0] = grid[n - 1][0]
    for r in range(n - 1, -1, -1):
        for c in range(m):
            if r == n - 1 and c == 0:
                continue
            val_from_down = dp_iahubina_to_rc[r + 1][c] if r < n - 1 else N_INF
            val_from_left = dp_iahubina_to_rc[r][c - 1] if c > 0 else N_INF

            if val_from_down != N_INF or val_from_left != N_INF:
                dp_iahubina_to_rc[r][c] = grid[r][c] + max(val_from_down, val_from_left)

    # --- Calculate dp_iahubina_from_rc (Iahubina from (r,c) to (0,m-1)) ---
    # This is equivalent to finding the path from (0,m-1) to (r,c) moving down/left.
    dp_iahubina_from_rc[0][m - 1] = grid[0][m - 1]
    for r in range(n):
        for c in range(m - 1, -1, -1):
            if r == 0 and c == m - 1:
                continue
            val_from_up = dp_iahubina_from_rc[r - 1][c] if r > 0 else N_INF
            val_from_right = dp_iahubina_from_rc[r][c + 1] if c < m - 1 else N_INF
            
            if val_from_up != N_INF or val_from_right != N_INF:
                dp_iahubina_from_rc[r][c] = grid[r][c] + max(val_from_up, val_from_right)

    max_total_gain_value = N_INF

    # Iterate through all possible meeting cells (r, c).
    # They must meet at an internal cell, meaning not on the border,
    # to allow both characters to move into it and out of it in valid directions.
    # The problem constraints (n, m >= 3) guarantee that such internal cells exist.
    for r in range(1, n - 1):  # r from 1 to n-2 (inclusive)
        for c in range(1, m - 1):  # c from 1 to m-2 (inclusive)
            # Scenario 1: Iahub passes vertically, Iahubina passes horizontally
            # Iahub's path: (0,0) -> ... -> (r-1,c) --- (meet at r,c) ---> (r+1,c) -> ... -> (n-1,m-1)
            # Iahubina's path: (n-1,0) -> ... -> (r,c-1) --- (meet at r,c) ---> (r,c+1) -> ... -> (0,m-1)
            
            # Get values for the four path segments surrounding the meet cell (r,c)
            path_segments_1 = [
                dp_iahub_to_rc[r - 1][c],      # Iahub's path to the cell just above (r,c)
                dp_iahub_from_rc[r + 1][c],     # Iahub's path from the cell just below (r,c)
                dp_iahubina_to_rc[r][c - 1],    # Iahubina's path to the cell just left of (r,c)
                dp_iahubina_from_rc[r][c + 1]   # Iahubina's path from the cell just right of (r,c)
            ]
            
            # Only consider this scenario if all four path segments are reachable
            if all(val != N_INF for val in path_segments_1):
                current_gain_1 = sum(path_segments_1)
                max_total_gain_value = max(max_total_gain_value, current_gain_1)

            # Scenario 2: Iahub passes horizontally, Iahubina passes vertically
            # Iahub's path: (0,0) -> ... -> (r,c-1) --- (meet at r,c) ---> (r,c+1) -> ... -> (n-1,m-1)
            # Iahubina's path: (n-1,0) -> ... -> (r+1,c) --- (meet at r,c) ---> (r-1,c) -> ... -> (0,m-1)
            path_segments_2 = [
                dp_iahub_to_rc[r][c - 1],      # Iahub's path to the cell just left of (r,c)
                dp_iahub_from_rc[r][c + 1],     # Iahub's path from the cell just right of (r,c)
                dp_iahubina_to_rc[r + 1][c],    # Iahubina's path to the cell just below (r,c)
                dp_iahubina_from_rc[r - 1][c]   # Iahubina's path from the cell just above (r,c)
            ]

            # Only consider this scenario if all four path segments are reachable
            if all(val != N_INF for val in path_segments_2):
                current_gain_2 = sum(path_segments_2)
                max_total_gain_value = max(max_total_gain_value, current_gain_2)

    # According to problem constraints (N, M >= 3 and grid[i][j] >= 0),
    # there will always be at least one valid meeting point and path configuration
    # leading to a non-negative total gain. Thus, max_total_gain_value should
    # never remain N_INF if input is valid.
    return max_total_gain_value
```