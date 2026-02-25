```python
from bisect import bisect_right
from sys import stdin, stdout


def solve(arr, queries):
    n = len(arr)
    l = [n+1]*n
    dp = [0]*(n+2)
    qresult = [0]*len(queries)
    
    for i in range(n):
        if n-arr[i]>=0:
            l[bisect_right(l,n-arr[i])] = n-arr[i]
    for i in range(n-1,-1,-1):
        dp[i] = max(dp[i+1],bisect_right(l,i+1))
        
    for q in range(len(queries)):
        qresult[q] = dp[queries[q][0]]

    return qresult
```