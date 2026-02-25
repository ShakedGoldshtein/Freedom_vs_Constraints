```python
def max_total_gain(n, m, matrix):
    dp1 = [[0]*m for _ in range(n)]
    dp2 = [[0]*m for _ in range(n)]
    dp3 = [[0]*m for _ in range(n)]
    dp4 = [[0]*m for _ in range(n)]
   
    for i in range(n):
        for j in range(m):
            if i > 0 or j > 0:
                dp1[i][j] = max(dp1[i-1][j], dp1[i][j-1]) + matrix[i][j]


    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i < n-1 or j < m-1:
                dp2[i][j] = max(dp2[i+1][j], dp2[i][j+1]) + matrix[i][j]


    for i in range(n-1, -1, -1):
        for j in range(m):
            if i < n-1 or j > 0:
                dp3[i][j] = max(dp3[i+1][j], dp3[i][j-1]) + matrix[i][j]


    for i in range(n):
        for j in range(m-1, -1, -1):
            if i > 0 or j < m-1:
                dp4[i][j] = max(dp4[i-1][j], dp4[i][j+1]) + matrix[i][j]

    
    total_gain = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            first = max(dp1[i-1][j] + dp2[i+1][j] + dp3[i][j-1] + dp4[i][j+1],
                         dp1[i][j-1] + dp2[i][j+1] + dp3[i+1][j] + dp4[i-1][j])
            total_gain = max(total_gain, first)

    return total_gain
```