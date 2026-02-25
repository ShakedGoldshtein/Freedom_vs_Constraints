```python
def solve_universe_coexistence(n, q, word, evolutions):
    religions = [[], [], []]
    result = []

    for evolution in evolutions:
        parts = evolution.split()
        if parts[0] == '+':
            i, c = int(parts[1]) - 1, parts[2]
            religions[i].append(c)
        else:
            i = int(parts[1]) - 1
            religions[i].pop()

        if not all(religions):
            result.append("YES")
            continue

        max_len = max(len(r) for r in religions)
        if max_len > n:
            result.append("NO")
            continue

        dp = [[[False] * (len(religions[2]) + 1) for _ in range(len(religions[1]) + 1)]
              for __ in range(len(religions[0]) + 1)]
        dp[0][0][0] = True

        for k in range(n):
            new_dp = [[[False] * (len(religions[2]) + 1) for _ in range(len(religions[1]) + 1)]
                      for __ in range(len(religions[0]) + 1)]
            for i in range(len(religions[0]) + 1):
                for j in range(len(religions[1]) + 1):
                    for l in range(len(religions[2]) + 1):
                        if not dp[i][j][l]:
                            continue
                        if i < len(religions[0]) and word[k] == religions[0][i]:
                            new_dp[i+1][j][l] = True
                        if j < len(religions[1]) and word[k] == religions[1][j]:
                            new_dp[i][j+1][l] = True
                        if l < len(religions[2]) and word[k] == religions[2][l]:
                            new_dp[i][j][l+1] = True
                        new_dp[i][j][l] = new_dp[i][j][l] or dp[i][j][l]
            dp = new_dp

        possible = dp[len(religions[0])][len(religions[1])][len(religions[2])]
        result.append("YES" if possible else "NO")

    return result
```