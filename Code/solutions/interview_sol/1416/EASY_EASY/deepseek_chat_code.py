```python
def solve(n, values):
    total = sum(values)
    target_size = n // 2
    if n % 2 == 0:
        target_size = n // 2
    else:
        target_size = (n - 1) // 2

    dp = [None] * (total + 1)
    dp[0] = []

    for i, val in enumerate(values):
        for s in range(total, val - 1, -1):
            if dp[s - val] is not None and (dp[s] is None or len(dp[s - val]) < len(dp[s])):
                if dp[s] is None or len(dp[s - val]) <= target_size:
                    new_list = dp[s - val] + [i]
                    if len(new_list) <= target_size + (n % 2):
                        dp[s] = new_list

    best_diff = float('inf')
    best_set = None
    for s in range(total + 1):
        if dp[s] is not None:
            set_size = len(dp[s])
            if n % 2 == 0 and set_size == target_size:
                diff = abs(2 * s - total)
                if diff < best_diff:
                    best_diff = diff
                    best_set = dp[s]
            elif n % 2 == 1 and (set_size == target_size or set_size == target_size + 1):
                diff = abs(2 * s - total)
                if diff < best_diff:
                    best_diff = diff
                    best_set = dp[s]

    han_set = []
    chewie_set = []
    han_indices = set(best_set)
    for i in range(n):
        if i in han_indices:
            han_set.append(values[i])
        else:
            chewie_set.append(values[i])

    if 0 not in han_indices:
        han_set, chewie_set = chewie_set, han_set

    return " ".join(map(str, han_set)) + "\n" + " ".join(map(str, chewie_set))
```