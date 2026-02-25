```python
def solve(H, W, grid):
    trans = [[0] * (W - 1) for _ in range(H - 1)]
    for i in range(H - 1):
        for j in range(W - 1):
            cnt = 0
            if grid[i][j] == '#':
                cnt += 1
            if grid[i+1][j] == '#':
                cnt += 1
            if grid[i][j+1] == '#':
                cnt += 1
            if grid[i+1][j+1] == '#':
                cnt += 1
            if cnt % 2 == 0:
                trans[i][j] = 1
    
    def largest_rectangle(heights):
        stack = []
        max_area = 0
        n = len(heights)
        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area
    
    max_rect = 0
    hist = [0] * (W - 1)
    for i in range(H - 1):
        for j in range(W - 1):
            if trans[i][j] == 1:
                hist[j] += 1
            else:
                hist[j] = 0
        max_rect = max(max_rect, largest_rectangle(hist))
    
    return max(max_rect + 1, 2)

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().splitlines()
    H, W = map(int, data[0].split())
    grid = data[1:1+H]
    print(solve(H, W, grid))
```