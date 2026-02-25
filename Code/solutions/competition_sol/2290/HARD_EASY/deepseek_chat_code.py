```python
def solve(H, W, grid):
    transposed = False
    if H > W:
        grid = [list(row) for row in zip(*grid)]
        H, W = W, H
        transposed = True
    
    black = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                black[i][j] = 1
    
    row_parity = [[0] * (W - 1) for _ in range(H)]
    for i in range(H):
        for j in range(W - 1):
            row_parity[i][j] = black[i][j] ^ black[i][j + 1]
    
    left = [[0] * (W - 1) for _ in range(H)]
    right = [[0] * (W - 1) for _ in range(H)]
    
    for j in range(W - 1):
        stack = []
        for i in range(H):
            while stack and row_parity[stack[-1]][j] == 0:
                stack.pop()
            left[i][j] = stack[-1] + 1 if stack else 0
            stack.append(i)
    
    for j in range(W - 1):
        stack = []
        for i in reversed(range(H)):
            while stack and row_parity[stack[-1]][j] == 0:
                stack.pop()
            right[i][j] = stack[-1] - 1 if stack else H - 1
            stack.append(i)
    
    max_area = 0
    for j in range(W - 1):
        for i in range(H):
            if row_parity[i][j] == 0:
                height = right[i][j] - left[i][j] + 1
                width = 2
                area = height * width
                if area > max_area:
                    max_area = area
    
    for i in range(H):
        consecutive = 0
        for j in range(W):
            if black[i][j] == 1:
                consecutive += 1
                max_area = max(max_area, consecutive)
            else:
                consecutive = 0
    
    for j in range(W):
        consecutive = 0
        for i in range(H):
            if black[i][j] == 1:
                consecutive += 1
                max_area = max(max_area, consecutive)
            else:
                consecutive = 0
    
    return max(max_area, 1)

def main():
    import sys
    data = sys.stdin.read().splitlines()
    H, W = map(int, data[0].split())
    grid = data[1:1+H]
    result = solve(H, W, grid)
    print(result)

if __name__ == "__main__":
    main()
```