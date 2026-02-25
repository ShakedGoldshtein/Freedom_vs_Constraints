```python
def solve(H, W, grid):
    def try_rectangle(state):
        max_area = 0
        for i1 in range(H):
            for i2 in range(i1, H):
                # Count consecutive 1s for each column between rows i1 and i2
                col_ones = [0] * W
                for j in range(W):
                    count = 0
                    for i in range(i1, i2+1):
                        if state[i][j] == 1:
                            count += 1
                    col_ones[j] = count
                    
                # Find max width of 1s
                curr_width = 0
                max_width = 0
                for ones in col_ones:
                    if ones == i2-i1+1:
                        curr_width += 1
                        max_width = max(max_width, curr_width)
                    else:
                        curr_width = 0
                        
                area = max_width * (i2-i1+1)
                max_area = max(max_area, area)
                
        return max_area

    # Convert input grid to 0/1
    grid = [[1 if c == '#' else 0 for c in row] for row in grid]
    
    max_area = 0
    # Try all row flips
    for row_state in range(1 << H):
        state = [row[:] for row in grid]
        # Flip rows according to state
        for i in range(H):
            if row_state & (1 << i):
                for j in range(W):
                    state[i][j] ^= 1
                    
        # For each column, determine if flipping maximizes black squares
        for j in range(W):
            blacks = sum(state[i][j] for i in range(H))
            if blacks < H-blacks:
                for i in range(H):
                    state[i][j] ^= 1
                    
        max_area = max(max_area, try_rectangle(state))
        
    return max_area
```