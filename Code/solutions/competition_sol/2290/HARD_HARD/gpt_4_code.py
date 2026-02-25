```python
def max_rectangle(grid: list) -> int:
    """Function to find the maximum possible area of a rectangle with a certain color."""
    H, W = len(grid), len(grid[0])
    hist = [[0]*W for _ in range(H+1)]
    
    for i in range(1, H+1):
        for j in range(W):
            if grid[i-1][j] == '#':
                hist[i][j] = 0
            else:
                hist[i][j] = hist[i-1][j] + 1
                
    max_area = 0

    for i in range(1, H+1):
        to_right = [0]*W
        to_left = [0]*W
        stack = []
        for j in range(W):
            while stack and hist[i][stack[-1]] >= hist[i][j]:
                stack.pop()
            to_left[j] = stack[-1] if stack else -1
            stack.append(j)
        stack.clear()
        for j in range(W-1, -1, -1):
            while stack and hist[i][stack[-1]] >= hist[i][j]:
                stack.pop()
            to_right[j] = stack[-1] if stack else W
            stack.append(j)
        
        for j in range(W):
            max_area = max(max_area, hist[i][j] * (to_right[j] - to_left[j] - 1))

    return max_area

H = 3
W = 3
grid = [
    ['.', '.', '#'],
    ['#', '#', '.'],
    ['.', '#', '.']
]

print(max_rectangle(grid))  # 6
```
This code defines a function which takes in a `grid` parameter, which is a list of lists representing the coloring of cells on a 2D game board. The function computes the histogram heights of each cell in the grid, and attempts to calculate the maximum possible area by checking the area of rectangles formed by expanding each cell horizontally. The result is then returned.