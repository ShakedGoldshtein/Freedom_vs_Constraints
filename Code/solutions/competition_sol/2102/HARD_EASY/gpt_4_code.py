```python
def solve(k):
    matrix = [[0] * 101 for _ in range(101)]
    n = min(100, 60)
    
    while int(n * (n - 1) * (n - 2) / 6) > k:
        n -= 1

    for i in range(2, n + 2):
        for j in range(1, i):
            matrix[i][j] = matrix[j][i] = 1
    
    k -= int(n * (n - 1) * (n - 2) / 6)
    
    for i in range(n + 2, 101):
        if k == 0:
            break
        for j in range(1, n + 1):
            if k < j:
                break
            matrix[i][j] = matrix[j][i] = 1
            k -= j
    
    matrix = matrix[1 : n + 2 + (k != 0)]
    matrix = [[str(cell) for cell in row[1 : n + 2 + (k != 0)]] for row in matrix]
    matrix = [''.join(row) for row in matrix]
    
    return str(n + (k != 0)) + '\n' + '\n'.join(matrix)

print(solve(1))
print(solve(10))
```