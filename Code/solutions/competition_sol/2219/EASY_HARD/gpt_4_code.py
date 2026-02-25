```python
def solve(n, q, s, queries):
    inf = 1e6
    nxt = [[inf] * 26 for _ in range(n + 2)]
    dp = [[[inf] * 251 for _ in range(251)] for _ in range(251)]
    dp[0][0][0] = -1
    s = '#' + s

    for i in range(n, 0, -1):
        nxt[i - 1] = nxt[i][:]
        nxt[i - 1][ord(s[i]) - ord('a')] = i

    r = [[0], [0], [0]]

    for query in queries:
        if query[0] == '+':
            _, i, c = query
            i, c = int(i) - 1, ord(c) - ord('a')
            r[i].append(c)
        else:
            _, i = query
            i = int(i) - 1
            r[i].pop()

        a, b, c = map(len, r)

        if query[0] == '-':
            dp[a][b][c] = inf if a * b * c > 0 else -1
            continue

        dp[a][b][c] = inf

        if a > 0:
            dp[a][b][c] = min(dp[a][b][c], nxt[dp[a - 1][b][c] + 1][r[0][a]])
        if b > 0:
            dp[a][b][c] = min(dp[a][b][c], nxt[dp[a][b - 1][c] + 1][r[1][b]])
        if c > 0:
            dp[a][b][c] = min(dp[a][b][c], nxt[dp[a][b][c - 1] + 1][r[2][c]])

        yield 'YES' if dp[a][b][c] <= n else 'NO'
```
Here are the calling arguments for above function:

```python
result = solve(6,8,'abbaab',[['+', '1', 'a'], ['+', '2', 'a'], ['+', '3', 'a'], ['+', '1', 'b'], ['+', '2', 'b'], ['+', '3', 'b'], ['-', '1'], ['+', '2', 'z']])
for i in result:
    print(i)

result = solve(6, 8,'abdabc',[['+', '1', 'a'], ['+', '1', 'd'], ['+', '2', 'b'], ['+', '2', 'c'], ['+', '3', 'a'], ['+', '3', 'b'], ['+', '1', 'c'], ['-', '2']])
for i in result:
    print(i)
```