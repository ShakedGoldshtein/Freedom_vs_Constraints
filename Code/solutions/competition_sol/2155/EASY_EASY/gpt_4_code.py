```python
def maximum_gain(n, m, gym):
    dp1 = [[0]*m for _ in range(n)]
    dp2 = [[0]*m for _ in range(n)]
    dp3 = [[0]*m for _ in range(n)]
    dp4 = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp1[i][j] = max(dp1[i-1][j], dp1[i][j-1]) + gym[i][j] if i+j else gym[i][j]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            dp2[i][j] = max(dp2[i+1][j], dp2[i][j+1]) + gym[i][j] if i+j!=n+m-2 else gym[i][j]
    for i in range(n-1,-1,-1):
        for j in range(m):
            dp3[i][j] = max(dp3[i+1][j], dp3[i][j-1]) + gym[i][j] if i+j!=n-1 else gym[i][j]
    for i in range(n):
        for j in range(m-1,-1,-1):
            dp4[i][j] = max(dp4[i-1][j], dp4[i][j+1]) + gym[i][j] if i+j!=m-1 else gym[i][j]
    res = float('-inf')
    for i in range(1,n-1):
        for j in range(1,m-1):
            res = max(res, dp1[i-1][j]+dp2[i+1][j]+dp3[i][j-1]+dp4[i][j+1], dp1[i][j-1]+dp2[i][j+1]+dp3[i+1][j]+dp4[i-1][j])
    return res
```
